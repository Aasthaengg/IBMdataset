h, w, a, b = map(int, input().split())

for i in range(h):
    if i < b:
        print('0' * a, end='')
        print('1' * (w-a))
    else:
        print('1' * a, end='')
        print('0' * (w-a))
