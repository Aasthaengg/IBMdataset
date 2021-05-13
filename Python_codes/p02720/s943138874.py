from heapq import heapify, heappop, heappush

def next_num(n):
    if n == 0:
        return [0, 1]
    elif n == 9:
        return [8, 9]
    else:
        return [n-1, n, n+1]

K = int(input())
queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]
heapify(queue)

for _ in range(K-1):
    now = heappop(queue)
    for next_i in next_num(now%10):
        heappush(queue, now*10 + next_i)

print(queue[0])