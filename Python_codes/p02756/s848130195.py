S = list(input())
Q = int(input())
a = 0
A = []
B = []
for i in range(Q):
  q = list(input().split())
  q[0] = int(q[0])
  if q[0] == 1:
    if a == 0:
      a = 1
    else:
      a = 0
  else:
    q[1] = int(q[1])
    if (q[1] == 1 and a == 0) or (q[1] == 2 and a == 1):
      B.append(q[2])
    else:
      A.append(q[2])
B = B[::-1]
ans = B + S + A
if a == 1:
  ans = ans[::-1]
ans = ''.join(ans)
print(ans)