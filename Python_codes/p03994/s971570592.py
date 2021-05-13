from bisect import *
S = list(str(input()))
K = int(input())

alp = list("abcdefghijklmnopqrstuvwxyz")

for i in range(len(S)):
  b = bisect_left(alp,S[i])

  if i == len(S)-1:
    S[i] = alp[(b+K)%26]
  elif b == 0:
    continue
  elif 26 - b <= K:
    K -= (26 - b)
    S[i] = "a"
  if K == 0:
    break
  
print("".join(S))