S = input()
ans = 0
buf = 0
for s in S:
  if s in ["A","T","G","C"]:
    buf += 1
  else:
    ans = max(ans, buf)
    buf = 0
print(max(ans, buf))