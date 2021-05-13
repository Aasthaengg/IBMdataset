
def check(N, c):
    RinRight = c.count('R')
    WinLeft = 0
    r = RinRight
    for i in range(N):
        if c[i] == 'R':
            RinRight -= 1
        else: # c[i] == 'W'
            WinLeft +=1
        r = min(r, max(RinRight,WinLeft))

    return r


N = int(input())
c= input()
print(check(N,c))