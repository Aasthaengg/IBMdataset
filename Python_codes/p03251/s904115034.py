n, m, x, y = map(int, input().split())
X = sorted(list(map(int, input().split())))
Y = sorted(list(map(int, input().split())))

z = X[-1] + 1
if z <= Y[0] and x < z <= y:
    print('No War')
else:
    print('War')
