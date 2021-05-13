n,k = map(int, input().split())
a=[]
while k>1:
    a.append(k)
    k/=2
a.append(k/2)
ans=0
c=0
b=n
while n>=1:
    if n>=a[c]:
        ans+=(2**(-c))*(1/b)
        n-=1
    else:
        c+=1
print(ans)
