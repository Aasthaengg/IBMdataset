n = int(input())
a = list(map(int, input().split()))
a.sort()
pd = True
for i in range(n-1):
  if a[i] == a[i+1]:
    pd = False
if pd: print('YES')
else: print('NO')