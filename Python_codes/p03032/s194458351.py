import heapq

n, k = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for i in range(min(n, k)+1):  # a+b
    for a in range(i+1):  # 操作A
        b = i - a  # 操作B
        L = V[:a] + V[n-b:]
        heapq.heapify(L)
        total = sum(L)
        for j in range(k-i):
            if not L:
                break
            if L[0] >= 0:
                break
            total -= heapq.heappop(L)
        ans = max(ans, total)

print(ans)