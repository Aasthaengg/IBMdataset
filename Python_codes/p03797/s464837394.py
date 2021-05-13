N,M = map(int,input().split())
ans = 0
ans += min(N,M//2)
M = M-2*ans
ans += M//4
print(ans)