n, t = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
same = 0
mn = 1100000000
dif = 0
for x in a:
  mn = min(mn, x)
  if dif == x - mn:
    ans += 1
  if dif < x - mn:
    dif = x - mn
    ans = 1
  
print(ans)