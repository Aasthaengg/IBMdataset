a,b,c = map(int,input().split())
l = []

for i in range(a,a+c):
  if i <= b:
    l.append(i)
for j in range(b,b-c,-1):
  if j >= a:
    l.append(j)
l = list(set(l))
l.sort()

for i in range(len(l)):
  print(l[i])