N = int(input())
A = list(map(int, input().split()))
A.sort()

S = [0]*(N+1)
for i in range(1, N+1):
    S[i] = S[i-1] + A[i-1]

for i in range(N)[::-1]:
    if S[i]*2 < A[i]:
        print(N-i)
        exit()