n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
p = 0

for ai in a:
  if p + ai > x:
    d = p + ai - x
    ans += d
    p = ai - d
  else:
    p=ai
    
print(ans)
