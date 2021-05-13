N = int(input())
A = list(map(int, input().split()))
D = [0 for i in range(N)]
D[1] = abs(A[0] - A[1])
for i in range(2, N):
  D[i] = min(D[i-2] + abs(A[i] - A[i-2]), D[i-1] + abs(A[i] - A[i-1]))
print(D[-1])