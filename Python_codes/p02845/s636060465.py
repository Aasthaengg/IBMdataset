n = int(input())
a = list(map(int, input().split()))
b = [0,0,0]
c = 1
for i in a:
  c = c*((b[0]==i)+(b[1]==i)+(b[2]==i))%(10**9+7)
  if b[0]==i:
    b[0] += 1
  elif b[1]==i:
    b[1] += 1
  else:
    b[2] += 1
print(c)