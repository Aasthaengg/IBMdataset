S = input()
K = int(input())
X = 0
i = 1
while i < len(S):
  if S[i] == S[i - 1]:
    X += 1
    i += 1
  i += 1
X *= K
if S == S[0] * len(S) and len(S) % 2 == 1:
  X += K // 2
elif i == len(S) and S[0] == S[-1]:
  x = 1
  i = 2
  while i < len(S):
    if S[i] == S[i - 1]:
      x += 1
      i += 1
    i += 1
  X += (K - 1) * (x - X // K)
print(X)
