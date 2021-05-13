S = list(input())
T = list(input())
res = 0
for i in range(len(S)):
  if S[i] == T[i]:
    res += 1
print(res)