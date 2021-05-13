N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
stf = 0

for i in range(N):
    stf += B[A[i] - 1]
    if A[i] - 1 == A[i - 1] and i > 0: 
        stf += C[A[i]-2]
        
        
print(stf)
