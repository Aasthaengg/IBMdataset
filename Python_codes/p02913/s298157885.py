import sys
readline = sys.stdin.readline

N = int(readline())
S = readline().rstrip()

def zalgo(S):
  N = len(S)
  res = [0] * N
  res[0] = N
  i = 1
  j = 0
  while i < N:
    while i + j < N and S[j] == S[i + j]:
      j += 1
    res[i] = j
    if j == 0:
      i += 1
      continue
    k = 1
    while i + k < N and k + res[k] < j:
      res[i + k] = res[k]
      k += 1
    i += k
    j -= k
  return res

res = 0
for i in range(N):
  T = S[i:]
  lcp = zalgo(T)
  for j in range(len(T)):
    l = min(lcp[j],j)
    if res < l:
      res = l

print(res)