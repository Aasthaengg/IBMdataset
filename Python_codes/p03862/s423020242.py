N, x = map(int, input().split())
a = list(map(int, input().split()))

res = 0
if a[0] > x:
    res += a[0]-x
    a[0] = x
for i in range(1,N):
    if a[i-1]+a[i] > x:
        tmp = a[i]+a[i-1]-x
        a[i] -= tmp
        res += tmp
print(res)