A, B = map(int, input().split())
print(100, 100)
G = [['.'] * 100 for _ in range(50)] + [['#'] * 100 for _ in range(50)]
for i in range(B - 1):
    G[(i // 50) * 2][(i % 50) * 2] = '#'
for i in range(A - 1):
    G[~((i // 50) * 2)][~((i % 50) * 2)] = '.'
for i in range(100):
    print(''.join(G[i]))