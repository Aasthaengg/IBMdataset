S = input()
N = len(S)
T = input()
M = len(T)

st = -1

for i in range(N-M, -1, -1):
  if all(S[i+j] in (T[j], "?") for j in range(M)):
    st = i
    break

newS = S.replace("?", "a")

if st == -1:
  print("UNRESTORABLE")
else:
  ans = ""
  for i in range(N):
    if st <= i <= st+M-1:
      ans += T[i-st]
    else:
      ans += newS[i]
  print(ans)