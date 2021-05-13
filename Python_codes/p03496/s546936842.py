n=int(input())
a=list(map(int,input().split()))
m=0
mi=1
ans=[0 for i in range(n+1)]
for i,z in enumerate(a,1):
    if(abs(z)>abs(m)):
        m=z
        mi=i
if(m>=0):
    ans[1]=[mi,1]
    for i in range(2,n+1):
        ans[i]=[i-1,i]
else:
    ans[1]=[mi,n]
    for i in range(2,n+1):
        ans[i]=[n-i+2,n+1-i]
print(2*n)
for i in ans[1:]:
    print(i[0],i[1])
    print(i[0],i[1])