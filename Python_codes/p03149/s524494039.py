n = [int(i) for i in input().split()]
n.sort()
a = set(n)
if 1 in a and 9 in a and 7 in a and 4 in a:
    print('YES')
else:
    print('NO')