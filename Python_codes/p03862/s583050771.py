n,x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
tmp = 0
tmp2 = 0
if a[0] > x:
    ans += a[0] - x
    tmp = x
else:
    tmp = a[0]
for i in range(1,n):
    if a[i] + tmp > x:
        tmp2 = a[i] + tmp - x
        ans += tmp2
        a[i] -= tmp2
        tmp = a[i]
    else:
        tmp = a[i]
print(ans)