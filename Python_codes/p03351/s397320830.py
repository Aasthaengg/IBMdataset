x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
l = sorted([a, b, c], reverse=True)
a_c = a - c
if a_c < 0:
  a_c = a_c*-1
if a_c <= d or ((l[0]-l[1] <= d) and (l[1]-l[2] <= d)):
  print('Yes')
else:
  print('No')