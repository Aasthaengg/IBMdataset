n = list(map(int, input().split()))
n.sort()
str_n = list(map(str, n))
if ''.join(str_n) == '1479':
    print('YES')
else:
    print('NO')