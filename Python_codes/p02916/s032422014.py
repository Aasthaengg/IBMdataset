N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
D=0
for i in range(0,len(A)-1):
    if A[i+1]==A[i]+1:
        D+=C[A[i]-1]
D+=sum(B)
print(D)