n,k = map(int,input().split())

min_ = k * (k-1) // 2
max_ = k * (2*n-k+1) // 2
ans = max_ - min_ + 1
ans = ans % (10**9+7)

if k == n+1:
    print(ans)

else:
    for i in range(k+1,n+2):
        min_ = min_ + (i-1)
        max_ = max_ + (n-(i-1))
        ans += max_ - min_ + 1
        ans = ans % (10**9+7)
    print(ans)