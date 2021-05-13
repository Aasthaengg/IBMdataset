N = int(input())
A = [int(input()) for _ in range(N)]
p = [0 for _ in range(N)]
for i in range(N):
  A[i] -= 1
  p[A[i]] = i
m = 0
prev = -1
cnt = 0
for i in range(N):
  if p[i] > prev:
    cnt += 1
  else:
    m = max(m, cnt)
    cnt = 1
  prev = p[i]
m = max(m, cnt)
print(N-m)