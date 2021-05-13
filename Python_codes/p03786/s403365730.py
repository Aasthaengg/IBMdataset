n=int(input())
a = sorted( list(map(int,input().split())) )
b=[0]*n
b[0]=a[0]
for i in range(n-1):b[i+1]=b[i]+a[i+1]
chk2 = [1 if b[i]*2>=a[i+1] else 0 for i in range(n-1)]
ans=0
while ans<n-1:
    if chk2[n-2-ans]==0:break
    ans+=1
print(ans+1)
