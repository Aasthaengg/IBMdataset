N,*D = map(int,open(0).read().split())

s = 0
ans = 0
for i in range(1,len(D)):
  s += D[i - 1]
  ans += D[i] * s
print(ans)
