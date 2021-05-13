k = int(input())
a,b = map(int,input().split())
x = 0

for i in range(a,b+1):
  if i%k == 0:
    print('OK')
    x = 1
    break

if x == 0:
  print('NG')