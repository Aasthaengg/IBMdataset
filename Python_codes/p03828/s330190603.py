n=int(input())
x=[0]*(n+1)
a=2
q=10**9+7
if n==1:
    print(1)
    exit()

for i in range(2,n+1):
    a=i
    p=2
    while p*p<=i:
        if a%p==0:
            x[p]+=1
            a=a//p
        else:
            p+=1
    if a!=1:
        x[a]+=1

ans=1
for i in range(n+1):
    ans=ans*(x[i]+1)%q
print(ans%q)

