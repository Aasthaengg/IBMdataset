_, a, b = map(int, open(0).read().split())
print('Borys' if (a - b) % 2 else 'Alice')