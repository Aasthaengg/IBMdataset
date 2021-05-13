S = input()
T = input()

ans = 1000
for start in range(len(S) - len(T) + 1):
  diff = 0
  for i in range(len(T)):
    if not T[i] == S[start + i]:
      diff += 1
  ans = min(ans, diff)
print(ans)