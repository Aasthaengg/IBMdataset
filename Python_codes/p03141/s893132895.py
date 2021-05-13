n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
x = []
for i in range(n):
  x.append((a[i][0]+a[i][1],i))
x.sort(reverse=True)
tk,ao = 0,0
for i in range(n):
  if i%2 == 0:
    tk += a[x[i][1]][0]
  else:
    ao += a[x[i][1]][1]
print(tk-ao)