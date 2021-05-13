n = int(input())
a = list(map(int,input().split()))
l,r = {},{}
for i in range(n):
  xl = i+a[i]
  if xl in l:
    l[xl] += 1
  else:
    l[xl] = 1
  
  xr = i-a[i]
  if xr in r:
    r[xr] += 1
  else:
    r[xr] = 1

ans = 0
for x in l:
  if x in r:
    ans += l[x] * r[x]
print(ans)