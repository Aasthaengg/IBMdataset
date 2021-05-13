N = int(input())
A = list(map(int, input().split()))
B = [0]*(N+1)
S = 0

for i in range(N):
    B[A[i]] += 1

for i in range(1, N+1):
    S += B[i]*(B[i]-1)//2

for k in range(N):
    print(S-B[A[k]]+1)