c = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))
c.extend(c2)
c.extend(c3)
for a1 in range(c[0]+1):
  b1 = c[0]-a1
  b2 = c[1]-a1
  b3 = c[2]-a1
  a2 = c[3]-b1
  a3 = c[6]-b1
  ab = [a1,a2,a3,b1,b2,b3]
  for i in ab:
    if i < 0:
      break
  if (c[4]==a2+b2) & (c[5]==a2+b3) & (c[7]==a3+b2) & (c[8]==a3+b3):
    print("Yes")
    break
else:
  print("No")