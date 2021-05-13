N, M = map(int,input().split())
ans = 0
if N >= M//2:
    ans = M//2
else:
    for i in range(max(0,M//2-N-10), max(0, M//2-N+10)):
        ans = max(ans,min(N+i//2,(M-i)//2))
print(ans)