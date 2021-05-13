N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
sum=0
for i in range(0,N):
    sum=sum+B[i]
    if i<=N-2 and A[i+1]-A[i]==1:
        sum=sum+C[A[i]-1]
    
print(sum)