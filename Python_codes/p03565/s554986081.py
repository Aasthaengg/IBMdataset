sd = input()
t = input()
n = len(sd)
m = len(t)
s = []
for i in range(n-m, -1, -1):
  ans = sd[i:i+m]
  for j in range(m + 1):
    if j == m :
      print((sd[:i] + t + sd[i + len(t):]).replace('?','a'))
      exit()
    if ans[j] == '?':
      continue
    elif ans[j] != t[j]:
      break
print("UNRESTORABLE")