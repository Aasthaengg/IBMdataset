n,m,l=map(int,input().split())
a=[]
b=[]
for i in range(n):
    a+=[list(map(int,input().split()))]

for i in range(m):
    b+=[list(map(int,input().split()))]
  
c=[]
c=[[sum(a[i][k]*b[k][j] for k in range(m))for j in range(l)] for i in range(n)]
[print(" ".join(list(map(str,c[i])))) for i in range(n)]