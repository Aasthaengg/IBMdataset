n,m = map( int,input().split() )
k = [ list(map( int,input().split() )) for _ in range(n) ]

c = [0] * (m+1)

for i in k:
  for j,data in enumerate(i):
    if j == 0:
      continue
    else:
      c[data] += 1

ans = 0
for i in c:
  if i == n:
    ans += 1

print(ans)
