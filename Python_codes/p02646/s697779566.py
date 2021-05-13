A, V = list(map(int,input().split()))
B, W = list(map(int,input().split()))
T = int(input())
if V <= W:
  print('NO')
elif abs(A-B) > abs(V-W) * T:
  print('NO')
else:
  print('YES')