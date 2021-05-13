c1= list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))

a1 = 0
a2 = c2[0] - c1[0]
a3 = c3[0] - c1[0]
b1 = c1[0]
b2 = c1[1]
b3 = c1[2]

if c1[0] == a1 + b1 and c1[1] == a1 + b2 and c1[2] == a1 + b3 and c2[0] == a2 + b1 and c2[1] == a2 + b2 and c2[2] == a2 + b3 and c3[0] == a3 + b1 and c3[1] == a3 + b2 and c3[2] == a3 + b3:
  print('Yes')
else:
  print('No')