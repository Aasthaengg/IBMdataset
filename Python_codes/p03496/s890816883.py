N = int(input())
A = [int(x) for x in input().split()]
cnt = 0
a_max = max(A + [0])
a_min = min(A + [0])
cnt = 0
S = []
if a_max + a_min >= 0:
  k = A.index(a_max)
  while A[0] < a_max:
    A[0] += a_max
    cnt += 1
    S += [[k + 1, 1]]
  for i in range(N - 1):
    while A[i + 1] < A[i]:
      A[i + 1] += A[i]
      cnt += 1
      S += [[i + 1, i + 2]]
else:
  k = A.index(a_min)
  while A[-1] > a_min:
    A[-1] += a_min
    cnt += 1
    S += [[k + 1, N]]
  for i in range(N - 1, 0, -1):
    while A[i - 1] > A[i]:
      A[i - 1] += A[i]
      cnt += 1
      S += [[i + 1, i]]
print(cnt)
for s in S:
  print(s[0], s[1])