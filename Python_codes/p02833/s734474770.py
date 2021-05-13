N = int(input())
ans = 0
if N % 2 == 0:
  a = N//10
  ans += a
  while a>1:
    a = a//5
    ans+=a
print(ans)
