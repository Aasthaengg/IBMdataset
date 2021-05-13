o = input()
e = input()
ans = ""
for i in range(1, len(o) + len(e) + 1):
  if i % 2 != 0:
    ans += o[int((i-1)/2)]
  else:
    ans += e[int((i-1)/2)]
print(ans)