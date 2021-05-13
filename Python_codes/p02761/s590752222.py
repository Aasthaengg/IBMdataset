n,m = map(int,input().split())
if m != 0:
    l = [list(map(int,input().split())) for i in range(m)]
    s,c = [list(i) for i in zip(*l)]
z = ['a'] * n
for i in range(m):
    if z[s[i]-1] == 'a':
        z[s[i]-1] = str(c[i])
    elif z[s[i]-1] == str(c[i]):
        pass
    else:
        print('-1')
        exit(0)
if n == 1:
    if z[0] == 'a':
        print(0)
    else:
        print(z[0])
else:
    if z[0] == '0':
        print(-1)
    else:
        if z[0] == 'a':
            z[0] = '1'
        for i in range(1,n):
            if z[i] == 'a':
                z[i] = '0'
        print(''.join(z))
