N = int(input())
A = list(map(int,input().split()))
A.sort()
S = [0] * N
total = 0
for i in range(N):
    total += A[i]
    S[i] = total
S = [0] + S
for i in range(1, N + 1):
    if A[-i] > 2 * S[-i - 1]:
        print(i)
        break