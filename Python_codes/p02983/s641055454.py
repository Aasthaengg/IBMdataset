l,r=map(int,input().split())

if r-l+1>=2019:
    print(0)
else:
    m=[]
    for i in range(l,r+1):
        m.append(i%2019)
    n=len(m)
    ans=10**9
    for i in range(n):
        for j in range(i+1,n):
            ans=min(ans,(m[i]*m[j])%2019)
    
    print(ans)