a, b, c = map(int, input().split())

i = 0
while i < 100:
  if (a*i-c)%b == 0:
    print('YES')
    exit()
  i += 1
print('NO')