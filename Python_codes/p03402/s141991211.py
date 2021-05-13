from itertools import product

a, b = map(int, input().split())

k = 50
s = [['.' for i in range(k)] + ['#' for i in range(k)] for j in range(2 * k)]

na = 1
for i, j in product(range(1, 2 * k - 1, 2), range(k + 1, 2 * k - 1, 2)):
    if na >= a:
        break
    s[i][j] = '.'
    na += 1

nb = 1
for i, j in product(range(1, 2 * k - 1, 2), range(1, k - 1, 2)):
    if nb >= b:
        break
    s[i][j] = '#'
    nb += 1

print(k * 2, k * 2)
for row in s:
    print(''.join(row))