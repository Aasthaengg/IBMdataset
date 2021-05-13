S = input()
ans = 0
p = ''
q = ''
for s in S:
  p += s
  if p != q:
    ans += 1
    q = p
    p = ''
print(ans)
