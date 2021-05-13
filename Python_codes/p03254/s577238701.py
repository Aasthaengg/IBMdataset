n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=-1
num=0
for i in range(n):
    num+=a[i]
    if num>x:
        ans=i
        break
if ans==-1:
    if num==x:
        print(n)
    else:
        print(n-1)
else:
    print(ans)
