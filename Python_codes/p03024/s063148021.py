s = input()
k = len(s)
cnt = s.count('o')
rem = 15 - k
if cnt + rem >= 8:
    print('YES')
else:
    print('NO')