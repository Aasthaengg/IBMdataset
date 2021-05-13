import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = LI()
mod = 10**9+7

ans = 1
x,y,z = -1,-1,-1
for i in range(N):
    a = A[i]
    k = [x,y,z].count(a-1)
    if k == 3:
        ans *= 3
        ans %= mod
        z += 1
    elif k == 2:
        ans *= 2
        ans %= mod
        if x == a-1:
            x = a
        elif y == a-1:
            y = a
        else:
            z = a
    elif k == 1:
        if x == a-1:
            x = a
        elif y == a-1:
            y = a
        else:
            z = a
    else:
        print(0)
        exit()

print(ans)
