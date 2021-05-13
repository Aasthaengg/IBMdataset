n=int(input())
*a,=map(int,input().split())
s=0
for i in range(1,n,1):
    d=a[i-1]-a[i]
    if d>0:
        s+=d
        a[i]+=d
print(s)