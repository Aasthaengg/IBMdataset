ans = 0
for s1, s2 in zip('CODEFESTIVAL2016', input()):
  if s1 != s2:ans += 1
print(ans)