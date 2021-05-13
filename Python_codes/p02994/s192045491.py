n,l=map(int,input().split())
A=[]
for i in range(n):
    A.append(l+i)
B=A.copy()
for j in range(len(B)):
    B[j]=abs(B[j])
print(sum(A)-A[B.index(min(B))])