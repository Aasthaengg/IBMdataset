# 13
A, B, C = input().split(' ')
count = 0
A = int(A)
B = int(B)
C = int(C)
a = A
b = B
c = C

while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
  N=[]
  N.append(B/2 + C/2)
  N.append(A/2 + C/2)
  N.append(A/2 + B/2)
  A = N[0]
  B = N[1]
  C = N[2]
  count += 1
  if A == a and B == b and C == c:
    print(-1)
    break
else:
  print(count)
