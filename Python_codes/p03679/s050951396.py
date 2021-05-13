x, a, b = list(map(int, input().split()))
d = b - a

if d <= 0:
  ans = 'delicious'
elif d <= x:
  ans = 'safe'
else:
  ans = 'dangerous'
print(ans)
