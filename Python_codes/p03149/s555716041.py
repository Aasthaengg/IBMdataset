n = list(map(str,input().split()))
n.sort()
ans = ''.join(n)

if ans == '1479':
    print('YES')
else:
    print('NO')