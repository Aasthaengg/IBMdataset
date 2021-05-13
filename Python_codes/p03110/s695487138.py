n = int(input())
ans = 0
for i in range(n):
  x,u = map(str,input().split())
  if u == 'JPY':
    x = int(x)
    ans += x
  else:
    x = float(x)
    ans += x*380000
print(ans)