l = input().split()
a = l[0][-1] == l[1][0]
b = l[1][-1] == l[2][0]
flag = a and b
if flag:
    print('YES')
else:
    print('NO')