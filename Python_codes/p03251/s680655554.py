n, m, x, y = map(int, input().split())
xn = list(map(int, input().split()))
ym = list(map(int, input().split()))

xn.sort()
ym.sort()

for z in range(x+1,y+1):
    if xn[-1]< z <=ym[0]:
        print('No War')
        exit()
print('War')
