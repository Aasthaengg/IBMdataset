A, B, T = map(int, input().split())
ans = 0
while T-A >= 0:
  T-= A
  ans += B
print(ans)