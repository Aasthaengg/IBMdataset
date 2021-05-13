s = input()
rest = 15 - len(s)
if s.count('o') + rest > 7:
    print('YES')
else:
    print('NO')