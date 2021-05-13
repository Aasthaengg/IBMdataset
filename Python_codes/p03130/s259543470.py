a = [list(map(int,input().split())) for _ in range(3)]
for i in range(1,5):
  if i in a[0] and i in a[1] and i in a[2]:
    print('NO')
    exit()
print('YES')