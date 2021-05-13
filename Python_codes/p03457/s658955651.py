N = int(input())
f = 0
a = 0
b = 1
c = 1
for i in range(N):
  a2, b2, c2 = map(int, input().split())
  dis = abs(b2 - b) + abs(c2 - c)
  dis_t = a2 - a
  if dis > dis_t or (dis_t - dis) % 2 == 1:
    f = 1
    break
  a = a2
  b = b2
  c = c2
if f == 1:
  print("No")
else:
  print("Yes")