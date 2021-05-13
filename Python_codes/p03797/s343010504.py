N,M = map(int,input().split())
if N > M:
    ans = (min(N,M//2))
elif M ==N:
    ans = (M//2)
else:
    tmp = M-2*N
    ans =N+(tmp//4)
print(ans)