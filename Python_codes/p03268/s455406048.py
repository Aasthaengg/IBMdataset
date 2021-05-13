N, K = map(int, input().split())

mod0, mod1 = 0, 0
for i in range(1, N+1):
    if i % K == 0:
        mod0 += 1
    elif i % K == K//2:
        mod1 += 1
        
if K%2 == 0:
    ans = mod0**3 + mod1**3
    print(ans)
else:
    ans = mod0**3
    print(ans)