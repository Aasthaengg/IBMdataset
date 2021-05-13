n,k,*ab = map(int,open(0).read().split())
ab = [(ab[i*2],ab[i*2+1]) for i in range(n)]
ab.sort(key = lambda x:x[0])
c = 0
for i,j in ab:
  c += j
  if c >= k:
    break
print(i)