n=int(input())
B=list(map(int,input().split()))
A=[B[0]]*n
for i in range(n-1):
    A[i+1]=B[i]
    A[i]=min(A[i],B[i])
print(sum(A))