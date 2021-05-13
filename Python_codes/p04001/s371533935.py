s=list(input())
n=len(s)
ans=0
for i in range(2**(n-1)):
    d=0
    s=list(x for x in s if x!="a")
    for j in range(n-1):
        if (i >> j)&1:
            s.insert(-j-1-d,"a")
            d+=1
    z="".join(s)
    y=list(map(int,z.split("a")))
    ans+=sum(y)
print(ans)
    
    
            
