def is_b(l):
    return all([a[i][j] in b for i, j in l])

a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]
t = [[(i, j) for j in range(3)] for i in range(3)]
t += [[(j, i) for j in range(3)] for i in range(3)]
t += [[(i, i) for i in range(3)]] + [[(2 - i, i) for i in range(3)]]
print('Yes' if any([is_b(ti) for ti in t]) else 'No')