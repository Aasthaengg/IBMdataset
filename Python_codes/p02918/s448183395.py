from bisect import bisect

N,K = map(int,input().split())
S = list(input())

f = S[0]

for i in range(N):
  if K == 0:
    break
  if S[i] != f:
    S[i] = f
    for j in range(i+1,N):
      if S[j] == f:
        break
      S[j] = f
    K -= 1
    
i = 0
res = 0

while i < N-1:
  f = S[i]
  for j in range(i+1,N):
    if S[j] != f:
      break
  else:
    res += 1
  res += j-i-1
  i = j
    
print(res)