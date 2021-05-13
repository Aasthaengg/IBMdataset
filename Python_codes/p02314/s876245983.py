import heapq

n, m = map(int, input().split())
coins = set(map(int, input().split()))


def fsp(n, coins):
    paid = [False] * (n + 1)
    paid[0] = True
    queue = list((1, v) for v in coins)
    heapq.heapify(queue)
    while queue:
        num, value = heapq.heappop(queue)
        if paid[value]:
            continue
        paid[value] = True
        for c in coins:
            new_value = value + c
            # Because of link cost is constant 1, it is reliably shortest-path.
            if new_value == n:
                return num + 1
            elif new_value > n or paid[new_value]:
                continue
            heapq.heappush(queue, (num + 1, value + c))


print(fsp(n, coins))