s = input()
ans = 10**18
for i in range(97,97+26):
  x = chr(i)
  ls = []
  tt = 0
  for j in s:
    if j != x:
      tt += 1
    else:
      ls.append(tt)
      tt = 0
  ls.append(tt)
  ans = min(ans,max(ls))
print(ans)