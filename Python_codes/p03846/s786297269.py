n=int(input())
a=list(map(int,input().split()))
b=[0]*(10**5)
mod=10**9+7
for i in range(n):
    b[a[i]]+=1
if n%2==0 and a.count(0)!=0:
    print(0)
    exit()
f=1
for i in range(n-1,-1,-2):
    if i==0:
        if b[i]!=1:
            f=0
            break
    elif b[i]!=2:
        f=0
        break
if f: 
    print(2**(n//2)%mod)
else: 
    print(0)