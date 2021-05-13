A,B,T = map(int,input().split())
ans = 0
second = 0
while second <= T - A:
  ans += B
  second += A
print(ans)