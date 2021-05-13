from itertools import groupby
S = input()
K = int(input())
if len(set(list(S)))==1:
  print(len(S)*K//2)
  exit()
ans = 0
L = []
for key, val in groupby(S):
  tmp = len(list(val))
  L.append(tmp)
sum_A = sum(k//2 for k in L)
ans = sum_A * K
if S[0] == S[-1]:
  ans += ((L[0]+L[-1])//2 - (L[0]//2+L[-1]//2))*(K-1)
print(ans)