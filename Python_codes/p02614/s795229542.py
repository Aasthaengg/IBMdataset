
h,w,k=map(int,input().split())
c=[[0]*w for i in range(h)]
d=[[0]*w for i in range(h)]
ans=0
for i in range(h):
    a=input()
    for j in range(w):
        c[i][j]=a[j]
for i in range(2**(h+w)):
    for m in range(h):
        for n in range(w):
            d[m][n]=c[m][n]
    for j in range(h):
        if (i >> j)&1:
            for x in range(w):
                d[j][x]="r"
    for j in range(h,w+h):
        if (i >> j)&1:
            for x in range(h):
                d[x][j-h]="r"
    f=0
    for q in range(h):
        for s in range(w):
            if d[q][s]=="#":
                f+=1
            
        
    if f==k:
        ans+=1
print(ans)

        
    
    
    
        
        
    
    
    
    
        
