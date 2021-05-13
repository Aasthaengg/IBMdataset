n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)
#print(a)
h=a[0]/2
dif=10**18
tmp=None
for i in range(1,n):
    if dif>abs(a[i]-h):
        dif=abs(a[i]-h)
        tmp=a[i]
print(a[0],tmp)