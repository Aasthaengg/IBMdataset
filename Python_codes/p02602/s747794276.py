n, k = map(int, input().split(' '))
a = [int(tmp) for tmp in input().split(' ')]
[print('Yes') if a < b else print('No') for a, b in zip(a[:n - k], a[k:])]