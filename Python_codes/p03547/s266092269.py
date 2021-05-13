x, y = input().split()
alpha = ['A', 'B', 'C', 'D', 'E', 'F']

if x == y:
    print('=')
else:
    if alpha.index(x) < alpha.index(y):
        print('<')
    else:
        print('>')
