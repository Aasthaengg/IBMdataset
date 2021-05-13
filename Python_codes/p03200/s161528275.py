S = list(map(str, input()))
ans = 0
L = []
for x, s in enumerate(S):
  if s == "B":
    L.append(x)
num = len(S) - len(L)
for l in L:
  ans += num - l
  num += 1
print(ans)