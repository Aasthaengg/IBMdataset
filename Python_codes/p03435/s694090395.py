c = [list(map(int, input().split())) for _ in range(3)]

a = sum(c[0]) + sum(c[1]) + sum(c[2])
b = c[0][0] + c[1][1] + c[2][2]

print('Yes' if a == 3 * b else 'No')