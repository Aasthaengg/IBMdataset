n,k,*a = map(int,open(0).read().split())
mod = 10**9+7
t1 = 0
for i in range(n-1):
  for j in range(i+1,n):
    if a[i]>a[j]:
      t1+=1
t2 = 0
c = 0
for i in sorted(list(set(a))):
  dc = a.count(i)
  t2 += c*dc
  c += dc
print((t1*k+t2*k*(k-1)//2)%mod)