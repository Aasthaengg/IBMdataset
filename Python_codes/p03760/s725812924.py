o = input()
e = input()

s = len(o)
t = len(e)
ans = ""
for i in range(s):
  ans += o[i]
  if s-t == 1 and i == s-1: break
  ans += e[i]
print(ans)