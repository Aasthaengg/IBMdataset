D = int(input())
C = input().split()
C = [int(c) for c in C]
#print(C)
S = []
for i in range(D):
  s = input().split()
  s = [int(j) for j in s]
  S.append(s)
M = 0
last = [0] * 26
#print(last)
for d in range(1,D+1):
  N = 0
  t = int(input())
  last[t-1] = d
  #print(last)
  for j in range(26):
    N = N + C[j]*(d-last[j])
  M = M + S[d-1][t-1] - N
  print(M)