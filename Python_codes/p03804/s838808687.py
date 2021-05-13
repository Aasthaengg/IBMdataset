n,m=map(int,input().split())
s=[input() for i in range(n)]
t=[input() for i in range(m)]

z=0
c=0

for i in range(n-m+1):
    for j in range(n-m+1): 
        
        for x in range(m):
            for y in range(m):
                if s[i+x][j+y]==t[x][y]:
                    z+=1
        if z==m**2:
            c+=1
        else:
            z=0
if c>0:
    print('Yes')
else:
    print('No')