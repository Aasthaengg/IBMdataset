a, b = map(int, input().split())
s = [['#'] * 100 for i in range(50)] + [['.'] * 100 for i in range(50)]
for i in range(a - 1):
    s[i * 2 // 100 * 2][i * 2 % 100] = '.'
for i in range(b - 1):
    s[51 + i * 2 // 100 * 2][i * 2 % 100] = '#'
print(100, 100)
for row in s:
    print(''.join(row))
