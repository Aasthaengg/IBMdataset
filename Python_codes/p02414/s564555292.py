n,m,l=map(int,input().split())
a=[]

for i in range(n):
    a.append([int(A) for A in input().split()])
    
b=[]
for i in range(m):
    b.append([int(B) for B in input().split()])

c=[]
L=[]
o=0
for i in range(l):
    for j in range(n):
        for k in range(m):
            o+=a[j][k]*b[k][i]
        c.append(o)
        o=0
    L.append(c[i*n:i*n+n])
    
for i in range(n) :
    for j in range(l) :
        if j == l - 1 :
            print(L[j][i])
        else :
            print(L[j][i], end = " ")
    
   

