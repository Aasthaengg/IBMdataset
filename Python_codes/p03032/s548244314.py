import heapq

N, K = map(int, input().split())
V = list(map(int, input().split()))
max_cnt = min(N, K)
ans = 0

for a in range(0, max_cnt + 1):
    for b in range(0, max_cnt + 1):
        if a + b > max_cnt:
            break
        if a == b == 0:
            continue
        hoseki = V[:a] + V[::-1][:b]
        heapq.heapify(hoseki)
        tmp = K - (a + b)
        while tmp and len(hoseki):
            my_min = heapq.heappop(hoseki)
            if my_min >= 0:
                heapq.heappush(hoseki, my_min)
                break
            tmp -= 1
        ans = max(ans, sum(hoseki))

print(ans)