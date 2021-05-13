n,m,l=map(int,input().split())
P=[]
Q=[]
R=[]
e=0

for i in range(1,n+1):
    P.append(input().split())
    
    
for j in range(1,m+1):
    Q.append(input().split())
   
    
for k in range(1,n+1):
    a=P[k-1]
    
    for p in range(1,m+1):
        b=Q[p-1]
        c=a[p-1]
        
        for q in range(1,l+1):
            d=int(c)*int(b[q-1])
            R.append(d)
          
    for r in range(l):
        for s in range(m):
            e+=R[r+l*s]
    
        if r<l-1:
            print(e,end=' ')
        else:
            print(e)
        e=0
    R=[]
