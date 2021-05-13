import sys
A, B, C = [int(x) for x in input().split()]
ans = 0
if(A==B==C)and(A%2==0)and(B%2==0)and(C%2==0):
  print(-1)
  sys.exit()
while (A%2==0)and(B%2==0)and(C%2==0):
  a = B/2 + C/2
  b = C/2 + A/2
  c = A/2 + B/2
  A, B, C = a, b, c
  ans += 1
print(ans)