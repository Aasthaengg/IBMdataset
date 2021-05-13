S = input()
L = list("ACGT")

ans = 0
t = 0
for i in range(len(S)):
  if S[i] in L:
    t += 1
    ans = max(t, ans)
  else:
    t = 0

print(ans)