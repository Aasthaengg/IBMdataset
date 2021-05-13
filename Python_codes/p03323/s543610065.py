a, b = map(int, input().split())

if abs(a-b) * 2 <= 16 - 2 * min(a, b):
    print('Yay!')
else:
    print(':(')