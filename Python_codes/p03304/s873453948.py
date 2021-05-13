N, M, D = map(int, input().split())

if D==0:
    dnum = N
else:
    dnum = 2*(N-D)
    
ans = dnum*(M-1) / N**2

print(ans)