N=int(input())
A=list(map(int,input().split()))
B=[0 for i in range(N+1)]
C=[0 for i in range(N+1)]
D=[0 for i in range(N+1)]
for i in range(N):
    B[A[i]]+=1
for i in range(1,N+1):
    C[i]=B[i]*(B[i]-1)//2
sum_=sum(C)
for i in range(1,N+1):
    print(sum_-B[A[i-1]]*(B[A[i-1]]-1)//2+(B[A[i-1]]-2)*(B[A[i-1]]-1)//2)