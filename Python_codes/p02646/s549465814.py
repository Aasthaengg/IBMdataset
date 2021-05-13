a, v = [int(i)  for i in input().split()]
b, w = [int(i)  for i in input().split()]
t = int(input())

if w >= v:
  print("NO")
  exit()
#print((b-a) / (v-w))

if b > a:
  if a + v*t >= b + w*t:
    print("YES")
  else:
    print("NO")
else :
  if a - v*t <= b - w*t:
    print("YES")
  else:
    print("NO")
