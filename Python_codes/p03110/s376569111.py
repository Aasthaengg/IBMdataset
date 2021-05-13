import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり

N = I()
xy = [LS() for _ in range(N)]

ans = 0
for i in range(N):
    x,y = xy[i]
    x = float(x)
    if y == 'JPY':
        ans += x
    else:
        ans += 380000*x

print(ans)