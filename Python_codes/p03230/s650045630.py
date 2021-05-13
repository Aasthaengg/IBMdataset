def issquare(n):
    f = (0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1)
    if f[n & 0xf]:
         return False
    l, r = 1, n
    while l <= r:
        m  = l + (r - l) // 2
        m2 = m * m
        if m2 < n:
            l = m + 1
        elif m2 > n:
            r = m - 1
        else:
            return True
    return False        

def istriangular(n):
    return issquare(1+8*n)

N = int(input())

if istriangular(N):
    print('Yes')
    n = int((1+8*N)**0.5-1) // 2
    k = n + 1
    print(k)
    base = 1
    for i in range(n):
        s = [n]
        base += i
        add = 0
        for j in range(n):
            s.append(base + add)
            if j < i:
                add += 1
            else:
                add += j + 1
        print(*s)
    s = [n, 1]
    for i in range(2, n+1):
        s.append(s[-1]+i)
    print(*s)
else:
    print('No')