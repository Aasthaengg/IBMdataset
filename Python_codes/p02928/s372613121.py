n, k = map(int, input().split())
a = list(map(int, input().split()))
p = 0 #tumble count in a: finally *k
q = 0 #tumble count between a: finally *kC2
for i in range(n-1):
  for j in range(i+1,n):
    if a[i] > a[j]:
      p += 1
for i in range(n):
  for j in range(n):
    if a[i] > a[j]:
      q += 1
p *= k
q *= k*(k-1)//2
print((p+q)%(10**9+7))