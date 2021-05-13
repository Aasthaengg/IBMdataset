N, M = map(int, input().split())
ans = min(M//2, N)
M = M - 2*ans
ans += M//4 
print(ans)