s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')
a, b, c = sorted([a, b, c])
if a==b==c:
    print('YES')
elif a==b and c-b < 2:
    print('YES')
elif b-a < 2 and b==c:
    print('YES')
else:
    print('NO')