A, V = list(map(int, input().strip().split()))
B, W = list(map(int, input().strip().split()))
T = int(input().strip())
ans = None

speed = V-W
if speed<=0:
  ans = 'NO'
else:
  distance = abs(A-B)
  if distance <= speed*T:
    ans = 'YES'
  else:
    ans = 'NO'

print(ans)