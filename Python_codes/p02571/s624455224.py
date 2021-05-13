S = input()
T = input()
ans = len(T)
for start in range(len(S) - len(T) + 1):
  dif = 0
  for i in range(len(T)):
    if T[i] != S[start + i]:
      dif += 1
  ans = min(ans, dif) 
print(ans)
