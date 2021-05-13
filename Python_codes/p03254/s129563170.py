n,x = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
ans = 0
for aa in a[:-1]:
  x -= aa
  if x >= 0:
    ans += 1
  else:
    break

if a[-1] == x:
  print(ans+1)
else:
  print(ans)