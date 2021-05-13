n,m=map(int,input().split())
a=[[] for i in range(n)]
b=[[] for i in range(m)]
f=0
for i in range(n):
    
    a[i]=list(input())
for i in range(m):
    b[i]=list(input())
for i in range(n-m+1):
    for j in range(n-m+1):
        ans=0
        for x in range(m):
            for y in range(m):
                if b[x][y]==a[x+i][y+j]:                 
                    ans+=1
        if ans==m*m:
            f=1
print("Yes" if f==1 else "No")
      
        
