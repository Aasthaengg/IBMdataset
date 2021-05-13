n,h = map(int,input().split())
s1 = []
s2 = []
for _ in range(n):
  a, b = map(int,input().split())
  s1.append(a)
  s2.append(b)
maxa = max(s1)
s2.sort(key=lambda x:-x)
ans = 0
for s2i in s2:
  if s2i > maxa:
    ans += 1
    h -= s2i
  if h <= 0:
    break
if h > 0:
  if h % maxa == 0:
    ans += h // maxa
  else:
    ans += h // maxa + 1
  print(ans)
else:
  print(ans)



