A, B = map(int, input().split())

K = 50
G = [['#' if i < K else '.'] * (2 * K) for i in range(2 * K)]

A -= 1
for i in range(0, 2 * K, 2):
    for j in range(0, 2 * K, 2):
        if A > 0:
            G[i][j] = '.'
            A -= 1
        else:
            break

B -= 1
for i in range(2 * K - 1, -1, -2):
    for j in range(2 * K - 1, -1, -2):
        if B > 0:
            G[i][j] = '#'
            B -= 1
        else:
            break

print (2 * K, 2 * K)
for g in G:
    print (*g, sep = '')

