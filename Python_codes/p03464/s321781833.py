#解説参照
k = int(input())
a = list(map(int, input().split( )))
l = 2
r = 2
for i in range(k-1,-1,-1):
    if (r//a[i])*a[i]<l:
        print(-1)
        exit()
    r2 = (r//a[i])*a[i]+a[i]-1
    l2 = ((l+a[i]-1)//a[i])*a[i]
    r = r2
    l = l2
print(l,r)