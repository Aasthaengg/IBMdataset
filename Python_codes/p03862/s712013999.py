n , x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(1,n):
    if a[i-1] + a[i] > x:
        p = a[i-1] + a[i] - x

        if a[i] - p >= 0:
            a[i] -= p
            ans += p
        elif a[i] - p < 0:
            a[i] = 0
            a[i-1] -= p - a[i]
            ans += p
print(ans)