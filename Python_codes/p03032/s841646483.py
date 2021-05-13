import sys

N, K = map(int, sys.stdin.readline().strip().split())
V = list(map(int, sys.stdin.readline().strip().split()))

ans=0
act = min(N, K)
for i in range(act + 1): # 左
    for j in range(N - act + i, N+1): # 右
        count = V[0:i] + V[j:N]
        count.sort()
        ans = max(ans, sum(count))
        for x in range(1, K - len(count) + 1): # 正負関係なく小さいものを捨てる 
            # print(sum(count[x:]))
            ans = max(ans, sum(count[x:]))
print(ans)