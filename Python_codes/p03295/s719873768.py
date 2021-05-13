n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(m)]
ab = sorted(ab, key=lambda x:(x[1],x[0]))

f = ab[0][1]
ans = 0
for a,b in ab:
  if a >= f:
    ans += 1
    f = b
    
print(ans+1)    