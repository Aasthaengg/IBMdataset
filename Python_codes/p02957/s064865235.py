A, B = map(int, input().split())
K = (B ** 2 - A ** 2) / (2 * A - 2 * B)
print(int(abs(K))) if K.is_integer() else print('IMPOSSIBLE')
