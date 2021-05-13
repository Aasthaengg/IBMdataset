S = input()
T = input()
def solve(i):
  flag = True
  for j in range(len(T)):
    if i+j < len(S) and (S[i+j] == "?" or S[i+j] == T[j]):
      continue
    else:
      flag = False
      break
  return flag
anslist = []
for i in range(len(S)):
  if solve(i):
    anstmp = S[:i] + T + S[i+len(T):]
    anstmp = anstmp.replace("?", "a")
    anslist.append(anstmp)
if len(anslist) > 0:
  anslist.sort()
  ans = anslist[0]
else:
  ans = "UNRESTORABLE"
print(ans)