mod=1000000007
n=int(input())
a=input()
b=input()
#1 22
#1
d=[1]
for i in range(1,n):
    if a[i-1]==a[i]:
        d[-1]+=1
    else:
        d.append(1)
ans=[3,6][d[0]-1]
for i in range(1,len(d)):
    if d[i-1]==d[i]==1:
        t=2
    elif d[i-1]==d[i]==2:
        t=3
    elif d[i-1]==2 and d[i]==1:
        t=1
    else:
        t=2
    ans=(ans*t)%mod
print(ans)
