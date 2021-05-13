S = list(input())
T = list(input())

ans = "z" * 100
for i in range(len(S) - len(T) +1)[::-1]:
  ok = True

  for j in range(len(T)):
    if S[i+j] != "?" and S[i+j] != T[j]:
      ok = False
  if ok:
    s = S[:i] + T + S[i+len(T):]
    s = "".join(s)
    ans = min(ans, s.replace("?", "a"))
    break
if ans == "z" * 100:
  print("UNRESTORABLE")
else:
  print(ans)