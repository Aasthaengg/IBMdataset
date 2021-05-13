# B - 1 Dimensional World's Tale

N, M, X, Y = map(int, input().split())
x = list(int(x) for x in input().split())
y = list(int(y) for y in input().split())

x_max = max(x)
x_max = max(x_max, X)
y_min = min(y)
y_min = min(y_min, Y)

if x_max < y_min:
    print('No War')
else:
    print('War')
