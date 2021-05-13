# ABC 059: B – Comparison
a, b = [input() for _ in range(2)]

if len(a) > len(b):
    print('GREATER')
elif len(a) < len(b):
    print('LESS')
else:
    if a > b:
        print('GREATER')
    elif a < b:
        print('LESS')
    else:
        print('EQUAL')