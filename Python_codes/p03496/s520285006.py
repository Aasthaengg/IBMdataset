N = int(input())
a = [int(c) for c in input().split()]
M = max(a)
Mi = a.index(M)
m = min(a)
mi = a.index(m)
ans = []
if 0<=m:
  for i in range(N-1):
    ans += [(i+1, i+2)]
elif M<=0:
  for i in range(N-1, 0, -1):
    ans += [(i+1, i)]
else:
  if abs(m)<abs(M):
    for i in range(N):
      if a[i]<0:
        ans += [(Mi+1, i+1)]
    for i in range(N-1):
      ans += [(i+1, i+2)]
  else:
    for i in range(N):
      if a[i]>0:
        ans += [(mi+1, i+1)]
    for i in range(N-1, 0, -1):
      ans += [(i+1, i)]

print(len(ans))
for c in ans:
  print(*c)