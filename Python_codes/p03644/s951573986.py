n=int(input())
q=0
ans=1
for i in range(1,n+1):
    m=i
    p=0
    while(m%2==0):
        m//=2
        p+=1
    if q!=max(q,p):
        ans=i
        q=max(q,p)
print(ans)