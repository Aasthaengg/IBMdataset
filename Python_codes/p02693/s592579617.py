K = int(input())
a,b = map(int, input().split())
for n in range(a, b + 1):
  if n % K == 0:
    print('OK')
    exit()
print('NG')