s = input().split()
a, b, c = int(s[0]), int(s[1]), int(s[2])
if b - a == c - b:
    print('YES')
else:
    print('NO')
