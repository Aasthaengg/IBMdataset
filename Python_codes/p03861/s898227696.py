a,b,x=map(int,input().split())
ans = 0
if a % x == 0:
  ans += 1
b //= x
a //= x
ans += b - a
print(ans)
