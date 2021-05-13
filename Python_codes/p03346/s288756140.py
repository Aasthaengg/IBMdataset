N = int(input())
P = []
for i in range(N):
  P.append(int(input()) - 1)

A = [0] * N
for i in range(N):
  A[P[i]] = i

ans,cnt = 0,0
work = -1
for i in range(N):
  if work < A[i]:
    cnt += 1
    ans = max(ans, cnt)
  else:
    cnt = 1
  work = A[i]

print(N-ans)