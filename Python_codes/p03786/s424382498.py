N = int(input())
A = list(map(int, input().split()))
A.sort()
S = [0 for _ in range(N)]
cnt = 1
S[0] = A[0]
for i in range(N-1):
  S[i+1] = A[i+1] + S[i]
for i in range(N-1, 0, -1):
  if A[i] <= 2 * S[i-1]:
    cnt += 1
  else:
    break
print(cnt)