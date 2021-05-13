def LI(): return list(map(int,input().split()))
N,x = LI()
a = LI()
ans = 0
for i in range(N-1):
    if a[i]+a[i+1]>x:
        if a[i]>x:
            ans += a[i+1]
            a[i+1] = 0
            ans += a[i]-x
        else:
            ans += a[i+1]-(x-a[i])
            a[i+1] = x-a[i]
print(ans)
