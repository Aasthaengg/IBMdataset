l = input().split()
a, b = list(map(int, l))
if a > b:
    c = '>'
elif a < b:
    c = '<'
else:
    c = '=='
print('a', c, 'b')