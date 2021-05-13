n = int(input())
a = []
b = []
for i in range(n):
  c, d= map(int, input().split())
  a.append(c)
  b.append(d)
a.reverse()
b.reverse()
tot = 0
for i in range(n):
  if (a[i]+tot)%b[i] == 0: continue
  x = b[i] - (a[i]+tot)%b[i]
  tot += x
print (tot)