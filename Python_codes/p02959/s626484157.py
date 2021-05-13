N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum_A=sum(A)
for i in range(N):
    if(B[i]>(A[i]+A[i+1])):
        A[i] -= A[i]
        B[i] -= A[i]
        A[i+1] -= A[i+1]
    elif(B[i]<=A[i]):
        A[i] -= B[i]
        B[i] -= B[i]
    elif(B[i]>=A[i]):
        B[i] -= A[i]
        A[i] -= A[i]
        A[i+1] -= B[i]
        B[i] -= B[i]
sum_end_A = sum(A)
print(sum_A-sum_end_A)