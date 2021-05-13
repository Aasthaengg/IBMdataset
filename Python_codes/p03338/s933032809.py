N = int(input())
S = input()
tmp = 0
for i in range(N):
  S1 = set(S[:i])
  S2 = set(S[i:])
  Sintcnt = len(S1 & S2)
  tmp = max(tmp, Sintcnt)
print(tmp)