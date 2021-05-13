x,y,z,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
BC=[]
ABC=[]
for b in range(y):
    for c in range(z):
        BC.append(B[b]+C[c])
A.sort(reverse=True)
BC.sort(reverse=True)

for a in range(x):
    for bc in range(min(k,y*z)):
        ABC.append(A[a]+BC[bc])
ABC.sort(reverse=True)
for i in range(k):
    print(ABC[i])