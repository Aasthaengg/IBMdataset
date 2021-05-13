# C - Low Elements
N = int(input())
P = list(map(int,input().split()))
m = N+1
ans = 0
for p in P:
    m = min(m,p)
    if p==m:
        ans += 1
print(ans)