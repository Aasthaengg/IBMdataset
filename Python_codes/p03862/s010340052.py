N, x = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
for k in range(1,N):
    if a[k-1] + a[k] > x:
        t = (a[k-1] + a[k]) - x
        ans += t
        if a[k] >= t:
            a[k] -= t
        else:
            a[k-1] -= t-a[k]
            a[k] = 0
print(ans)
