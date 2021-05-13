#16:00
n,m = map(int,input().split())
a = list(map(lambda x:int(x)-1,input().split()))
pre = [i for i in range(n)]
for _ in range(m):
  X,Y = map(int,input().split())
  X -= 1
  Y -= 1
  while pre[X] != X:
    X = pre[X]
  while pre[Y] != Y:
    Y = pre[Y]
  if X == Y:
    continue
  elif X < Y:
    pre[Y] = X
  else:
    pre[X] = Y
#print(a)
#print(pre)
region = [[] for _ in range(n)]
ser = [[] for _ in range(n)]
for i in range(n):
  b = a[i]
  I = i
  while pre[I] != I:
    I = pre[I]
  region[I].append(b)
  ser[I].append(i)
#print(region)
#print(ser)
home = [10**6 for _ in range(n)]
mother = [10**6 for _ in range(n)]
for i in range(n):
  for x in region[i]:
    home[x] = i
for i in range(n):
  for y in ser[i]:
    mother[y] = i
#print(home)
#print(mother)
ans = []
for i in range(n):
  if home[i] == mother[i]:
    ans.append(i)
#print(ans)
print(len(ans))