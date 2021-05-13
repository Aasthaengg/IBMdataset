r, D, x2000 = map(int, input().split())

xs = []
x = x2000
for _ in range(10):
    x = r*x - D
    xs.append(x)

print('\n'.join(map(str, xs)))
