import sys
A, B = map(int, input().split())
tmp = 0

if (abs(A)-abs(B))%2 == 1:
  print("IMPOSSIBLE")
  sys.exit()

if A < B:
  tmp = A
  A = B
  B = tmp

if A > 0 and B > 0:
  K = (A+B)/2
elif A < 0 and B < 0:
  K = -(abs(A)+abs(B))/2
else:
  K = A-(abs(A)+abs(B))/2

print(int(K))