string = input()
a, b = map(int, (string.split(' ')))
if a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    print('a == b')
