values = input()
a, b, c = [int(x) for x in values.split()]
if a < b and b < c:
    print('Yes')
else:
    print('No')