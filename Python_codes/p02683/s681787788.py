n,m,x = map(int,input().split())
a = []
c = []
for i in range(n):
  a.append(list(map(int,input().split())))
  c.append(a[i])
  
p = []
for i in range(2 ** (n)):
    tmp = [0] * (n)
    for j in range(n):
        if i >> j & 1:
            tmp[j] = 1
    p.append(tmp)
ans = []

for i in range(len(p)):
  tmp = 0
  tmp2 = [0]*m
  tmp3 = 0
  for j in range(len(p[i])):
    if p[i][j] == 1:
      tmp += a[j][0]
      for k in range(m):
        tmp2[k] += a[j][k+1]
  for k in range(m):
    if tmp2[k] >= x:
      tmp3 += 1
  if tmp3 == m:
    ans.append(tmp)
  #print(tmp2)
  
if len(ans) == 0:
  print(-1)
else:
  print(min(ans))