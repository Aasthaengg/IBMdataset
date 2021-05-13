# 頭から順にaに変えていく

import sys
readline = sys.stdin.readline

S = list(readline().rstrip())
K = int(readline())

z = ord("z")
for i in range(len(S) - 1):
  # aにするためのコストを求める
  if S[i] == "a":
    continue
  cost = z + 1 - ord(S[i])
  if cost <= K:
    S[i] = "a"
    K -= cost

K %= 26
nex = ord(S[-1]) + K
if nex > ord("z"):
  nex -= 26
S[-1] = chr(nex)

print("".join(S))
