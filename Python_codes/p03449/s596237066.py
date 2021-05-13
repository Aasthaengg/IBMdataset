import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S_A = [0]*(N+1)
S_B = [0]*(N+1)
for i in range(N):
    S_A[i+1] = S_A[i] + A[i]
    S_B[i+1] = S_B[i] + B[i]
X = [0]*N
X[0] = A[0]+B[0]
for i in range(N-1):
    X[i+1] = max(X[i]+B[i+1],S_A[i+2]+B[i+1])
    
print(X[N-1])