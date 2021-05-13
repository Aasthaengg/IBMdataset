a, b = map(int, open(0).read().split())
if a > b:
    print('GREATER')
elif a < b:
    print('LESS')
else:
    print('EQUAL')