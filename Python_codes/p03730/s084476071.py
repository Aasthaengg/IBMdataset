A, B, C = map(int, input().split())

for i in range(100):
  if ((C+B*i)/A).is_integer():
    print('YES')
    exit()
print('NO')