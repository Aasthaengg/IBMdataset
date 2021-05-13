n = list(map(int, input().split(' ')))
n.sort()
n1 = n[0]
n2 = n[3]
n3 = n[2]
n4 = n[1]
if n1 == 1 and n2 == 9 and n3 == 7 and n4 == 4:
    print('YES')
else:
    print('NO')
