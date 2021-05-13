N=int(input())
B=list(map(int,input().split()))
A=[]
for c in B:
    A.append(c)
A.append(B[-1])

for a in range(len(B)):
   
    if A[a]>B[a]:
        A[a]=B[a]
    elif A[a+1]>B[a]:
        A[a+1]=B[a]

print(sum(A))