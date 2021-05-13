a,b,c = map(str, input().split())
an = len(a)
bn = len(b)

if a[an-1] == b[0]:
  if b[bn-1] == c[0]:
    print('YES')
    exit()
print('NO')