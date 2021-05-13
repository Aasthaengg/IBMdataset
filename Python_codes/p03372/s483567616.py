n,c = map(int,input().split())
sushi = []
for _ in range(n):
  sushi.append(list(map(int,input().split())))
can = []

right1 = []
right2 = []
tmp = 0
for i in range(n):
  s,v = sushi[i]
  tmp += v
  right1.append([tmp-s,s])
  right2.append([tmp-2*s,s])
left1 = []
left2 = []
tmp = 0
for i in range(n)[::-1]:
  s,v = sushi[i]
  tmp += v
  left1.append([tmp-(c-s),c-s])
  left2.append([tmp-2*(c-s),c-s])
right1.sort()
left1.sort()
#print(right1)
#print(left1)

can.append(0)
can.append(right1[-1][0])
can.append(left1[-1][0])
#print(can)
for i in range(n):
  energy,s = right2[i]
  while left1[-1][1] + s >= c:
    left1.pop()
    if left1 == []:
      break
  else:
    can.append(energy + left1[-1][0])
    #print(s,left1[-1][1],left1)
    continue
  break
#print(can)
for i in range(n):
  energy,s = left2[i]
  while right1[-1][1] + s >= c:
    right1.pop()
    if right1 == []:
      break
  else:
    can.append(energy + right1[-1][0])
    #print(s,right1[-1][1],right1)
    continue
  break
print(max(can))
#print(can)