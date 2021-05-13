a=[int(i) for i in input().split()]
a.sort()
print('YES' if a[2]-a[1]==a[1]-a[0] else 'NO')
