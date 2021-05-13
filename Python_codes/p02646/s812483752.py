A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

ans = 'NO'
distance = abs(B-A)
if V == W:
  pass
else:
  t = distance/(V-W)
  if 0 < t <= T:
    ans = 'YES'

print(ans)