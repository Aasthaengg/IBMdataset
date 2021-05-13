x, y = input().split()

hex = ['A', 'B', 'C', 'D', 'E', 'F']

xi = hex.index(x)
yi = hex.index(y)

if xi < yi:
    print('<')
elif xi > yi:
    print('>')
else:
    print('=')
