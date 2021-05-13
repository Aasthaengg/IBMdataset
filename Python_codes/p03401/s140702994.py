N = int(input())
A = list(map(int, input().split()))

S = [abs(A[0])]
for i in range(N-1):
  S.append(S[-1] + abs(A[i+1] - A[i]))
S.append(S[-1] + abs(A[N-1]))

for i in range(N):
  if i == 0:
    ans = S[N] - S[1] + abs(A[1])
    print(ans)
  elif i == N-1:
    ans = S[N-2] + abs(A[N-2])
    print(ans)
  else:
    ans = S[i-1] + (S[N] - S[i+1]) + abs(A[i+1] - A[i-1])
    print(ans)

