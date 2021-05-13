N = list(input().split())

N.sort()

if N[0]+N[2]+N[3]+N[1] == '1794':
    print('YES')
else:
    print('NO')
