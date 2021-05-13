import sys
input = sys.stdin.readline
S = list(input())[: -1]
K = int(input())
a = ord("a")
N = len(S)
for i in range(N):
  x = ord(S[i])
  if K >= (a - x) % 26:
    K -= (a - x) % 26
    S[i] = "a"
S[-1] = chr((ord(S[i]) - a + K % 26) % 26 + a)
print("".join(S))