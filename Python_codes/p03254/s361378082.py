N,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
c = 0
rx = x
for i in range(N):
  if a[i] > rx or (i == N-1 and rx != a[i]):
    print(c)
    exit()
  c += 1
  rx -= a[i]
print(N)