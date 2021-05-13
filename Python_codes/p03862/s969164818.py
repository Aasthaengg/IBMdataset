N,x = map(int,input().split())
a = list(map(int,input().split()))

res = 0
if a[0]>x:
    res = a[0]-x
    a[0] = x
for i in range(1,N):
    tmp = a[i]+a[i-1]-x
    if tmp > 0:
        a[i] -= tmp
        res += tmp
print(res)


