n,m=map(int,input().split())
ab=[[] for i in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    ab[i].append(a)
    ab[i].append(b)

ab=sorted(ab)
ans=0
d=m

for i in range(n):
    if ab[i][1]<=d:
        ans+=ab[i][0]*ab[i][1]
        d-=ab[i][1]
    else:
        
        ans+=ab[i][0]*d
        
        break
print(ans)
        
        
    
