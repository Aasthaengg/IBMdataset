n,m =map(int,input().split())
 
H=[]
H=list(map(int,input().split()))
C=[]
for i in range(n):
    C.append(1)
 
for i in range(m):
    a,b = map(int,input().split())
    if H[a-1]==H[b-1] :
        C[a-1] = 0
        C[b-1] = 0
    elif H[a-1]<H[b-1] :
        C[a-1] = 0
    else:
        C[b-1] = 0
 
print( C.count(1))      
