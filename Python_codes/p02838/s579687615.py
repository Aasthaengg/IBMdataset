n=int(input())
A=list(map(int,input().split()))
ans=0
for d in range(61):
    n_1 = 0
    for a in A:
        if (a>>d)&1 == 1:
            n_1 += 1
    n_0 = n - n_1
        
    ans += n_0*n_1 * 2**d
    ans %= 10**9+7
print(ans)