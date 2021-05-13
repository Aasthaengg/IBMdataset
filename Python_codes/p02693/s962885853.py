a = int(input())
c, d = map(int, input().split())
for i in range(c, d+1):
  if i % a == 0:
    print('OK')
    exit()
print('NG')