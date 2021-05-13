a, b, c ,k = map(int,input().split())
ans = 0
if a<=k:
  ans += a
  k -=a
else:
  print(k)
  exit()

if b<k:
  k -=b
else:
  print(ans)
  exit()

if c<=k:
  ans -=c
else:
  ans -= k
print(ans)