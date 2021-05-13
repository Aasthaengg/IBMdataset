K, X = map(int, input().split(' '))
for i in range(X - K + 1, X + K - 1):
  print('{} '.format(i), end='')
print(X + K - 1)