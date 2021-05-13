mod=1000000007
n=int(input())
a=input()

d=[0]
for i in range(1,n):
    if a[i-1]==a[i]:
        d[-1]+=1
    else:
        d.append(0)
ans=[3,6][d[0]]
for i in range(1,len(d)):
    if d[i-1]==d[i]==1:
        t=3
    elif d[i-1]==1 and d[i]==0:
        t=1
    else:
        t=2
    ans=(ans*t)%mod
print(ans)