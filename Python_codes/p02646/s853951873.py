A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if A == B:
  print('YES')
elif V <= W:
  print('NO')
elif (V-W) * T >= abs(A-B):
  print('YES')
else:
  print('NO')
