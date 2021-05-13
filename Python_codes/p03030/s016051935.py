n = int(input())
sp = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
  sp[i][1] = int(sp[i][1]) * -1
x = sorted(sp)
for i in range(n):
  print(sp.index(x[i])+1)