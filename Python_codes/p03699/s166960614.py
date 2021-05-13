n = int(input())
s = sorted([int(input()) for i in range(n)])
ans = sum(s)
d = ans
for i in s:
  if i % 10 != 0:
    d = i
    break
if ans % 10 != 0:
  print(ans)
else:
  print(ans - d)
