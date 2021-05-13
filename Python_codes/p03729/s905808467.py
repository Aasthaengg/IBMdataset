a = list(map(str,input().split()))
flag = 0

if a[0][len(a[0])-1] == a[1][0] and a[1][len(a[1])-1] == a[2][0]:
    print('YES')
else:
    print('NO')
