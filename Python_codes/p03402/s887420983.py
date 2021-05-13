A, B = map(int, input().split())
K = 50
G = [['.' for j in range(2 * K)] for i in range(K)] + [['#' for j in range(2 * K)] for i in range(K)]
x = 0
while B > 1:
  for y in range(min(K, B - 1)):
    G[x][x % 2 + 2 * y] = '#'
    B -= 1
  x += 2
x = 2 * K - 1
while A > 1:
  for y in range(min(K, A - 1)):
    G[x][x % 2 + 2 * y] = '.'
    A -= 1
  x -= 2
print(2 * K, 2 * K)
for i in range(2 * K):
  print(''.join(G[i]))