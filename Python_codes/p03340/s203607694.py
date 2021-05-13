#14:50
#チョイ見た
scale = 20
#scale = 3
n = int(input())
raw = list(map(int,input().split()))
a = [[] for _ in range(scale)]
for i in range(n):
  x = raw[i]
  for d in range(scale):
    a[d].append(x%2)
    x //= 2
#print(a)
c = []
for d in range(scale):
  b = []
  tmp = 0
  for i in range(n):
    if a[d][i] == 1:
      tmp += 1
      if tmp == 2:
        b.append(i)
        break
  else:
    b += [n for _ in range(n)]
    c.append(b)
    continue
  for i in range(1,n):
    if a[d][i-1] == 0:
      b.append(b[-1])
      continue
    for j in range(b[-1]+1,n):
      if a[d][j] == 1:
        b.append(j)
        break
    else:
      b += [n for _ in range(i,n)]
      break
  c.append(b)
#print(c)
ans = []
for l in range(n):
  now = []
  for d in range(scale):
    now.append(c[d][l])
  ans.append(min(now)-l)
#print(ans)
print(sum(ans))