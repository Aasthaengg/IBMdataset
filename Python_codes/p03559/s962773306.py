n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
c = sorted(list(map(int,input().split())))
bn = [0]*n
j = 0
for i in range(n):
  bi = b[i]
  while(j<n):
    if bi < c[j]:
      bn[i] = n-j
      break
    j += 1
bnt = sum(bn)
bs = 0
j = 0
ans = 0
for i in range(n):
  ai = a[i]
  while(j<n):
    if ai < b[j]:
      ans += bnt - bs
      break
    bs += bn[j]
    j += 1
print(ans)