m = input()
m = list(m)
m = list(map(int,m))
for i in range(2**3):
    n = m[0]
    x = i
    t = []
    for _ in range(3):
        if x % 2 != 0:
            n += m[_+1]
            t.append('+')
        else:
            n -= m[_+1]
            t.append('-')
        x = x // 2
    if n == 7:
        l = [m[0],t[0],m[1],t[1],m[2],t[2],m[3],'=',7]
        l = list(map(str,l))
        print(''.join(l))
        break