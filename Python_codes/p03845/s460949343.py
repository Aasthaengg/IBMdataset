n = int(input())
t = list(map(int, input().split()));
m = int(input())
p, x = [0] * m, [0] * m
for i in range(m) :
  p[i], x[i] = map(int, input().split())

for i in range(m) :
  res = 0
  for j in range(n) :
    if j+1 == p[i] : 
      res += x[i]
    else :
      res += t[j]
  print(res)