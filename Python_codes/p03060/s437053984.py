N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

A = [0 for i in range(N)]

for i in range(N):
     A[i] = V[i]-C[i]

A = sorted(A)[::-1]

ans = 0

for i in range(N):
  if A[i] > 0:
    ans += A[i]
  else:
    break

print(ans)