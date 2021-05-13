a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
x = abs(b - a)
ans = ''
if v <= w:
  ans = 'NO'
else:
  if x / (v - w) <= t:
    ans = 'YES'
  else:
    ans = 'NO'
print(ans)