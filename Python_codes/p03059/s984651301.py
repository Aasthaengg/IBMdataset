a, b, t = map(int, input().split())
ans = 0
if(b <= t):
  while(a*ans < t + 0.5):
    ans += 1
else:
  ans = 1
print((ans-1) * b)