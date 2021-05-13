n=int(input())
a=list(map(int,input().split()))
ave=0
for i in range(n):
    ave+=a[i]
ave/=n
if ave in a:
    ans=a.index(ave)
    print(ans)
else:
    min=101
    for i in range(n):
        gap=abs(ave-a[i])
        if min>gap:
            min=gap
            num=a[i]
    print(a.index(num))
