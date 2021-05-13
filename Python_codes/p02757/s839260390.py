import sys
n,p=map(int,input().split())
s=list(input())
if p==2 or p==5:
    ans=0
    for i in range(n):
        if int(s[i])%p==0:
            ans+=i+1
    print(ans)
    sys.exit(0)
ans=0
count=[0]*p
count[0]=1
s=s[::-1]
num=0
seki=1
for i in range(n):
    num+=int(s[i])*seki
    num=num%p
    count[num]+=1
    seki=seki*10
    seki=seki%p
for i in range(p):
    N=count[i]
    ans+=N*(N-1)//2
print(ans)
#print(count)