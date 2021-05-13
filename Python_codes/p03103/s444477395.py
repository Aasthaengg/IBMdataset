import sys
n,m=map(int,input().split())
ab=[]
for i in range(n):
    ab.append(list(map(int,input().split())))

ab=sorted(ab,key=lambda x:x[0])

ans=0
for i in range(n):
    c=ab[i][1]
    if c<m:
        ans+=ab[i][0]*c
        m-=c
    else:
        ans+=ab[i][0]*m
        print(ans)
        sys.exit()
        
    
