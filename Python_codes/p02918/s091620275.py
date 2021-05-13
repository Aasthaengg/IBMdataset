n,k=map(int,input().split())
s=input()
t=s[0]
ans=0
u=0
f=True
for i in range(1,n):
    if t==s[i]:
        ans+=1
    else:
        t=s[i]
        if f:
            f=False
        else:
            f=True
            u+=1
if k<=u:
    ans+=2*k
if k>u:
    ans=n-1
print(ans) 