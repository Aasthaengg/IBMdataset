from collections import Counter as c
N = int(input())
S = list(input() for _ in range(N))
S.sort()
C, i = c(S).most_common(), 0
l, n = len(C), C[0][1]
while i < l:
  if n == C[i][1]: print(C[i][0])
  else: break
  i += 1