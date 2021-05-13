def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c


N = int(input())
X = input()
pc = X.count('1')
if pc == 0:
    for i in range(N):
        print(1)
elif pc == 1:
    if X[-1] == '1':
        for i in range(N-1):
            print(2)
        print(0)
    else:
        for i in range(N-1):
            if X[i] == '1':
                print(0)
            else:
                print(1)
        print(2)
else:
    modX1 = 0
    modX2 = 0
    Xi = [None] * N
    x1 = 1
    x2 = 1
    for i in range(N):
        if X[-i-1] == '1':
            Xi[-i-1] = x1
            modX1 = (modX1+x1) % (pc-1)
            modX2 = (modX2+x2) % (pc+1)
        else:
            Xi[-i-1] = x2
        x1 = x1 * 2 % (pc-1)
        x2 = x2 * 2 % (pc+1)
    for i in range(N):
        ans = 1
        x = (modX1 - Xi[i]) % (pc-1) if X[i] == '1' else (modX2 + Xi[i]) % (pc+1)
        while x != 0:
            x = x % popcnt(x)
            ans += 1
        print(ans)