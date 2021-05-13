a, b, c = map(int, input().split())
temp = 0
for i in range(20000):
  temp = (temp + a) % b
  if temp == c:
    print('YES')
    exit()
print('NO')