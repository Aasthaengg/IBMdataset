a = list(map(int, input().split()))
a.sort()
if a[2]-a[1]==a[1]-a[0]: print('YES')
else: print('NO')