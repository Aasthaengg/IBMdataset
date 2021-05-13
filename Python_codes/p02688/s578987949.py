n,k =map(int,input().split())

D=[]
A=[]
C=[]
for i in range(k):
    D.append(int(input()))
    A.append(list(map(int,input().split())))
for i in range(1,n+1):
    C.append(int(i))

for i in range(k):
    for a in A[i]:
        if C.count(a)!=0:
            C.remove(a)
        
print( len(C) )

