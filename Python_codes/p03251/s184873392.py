n, m, x, y = map(int, input().split())
xx = list(map(int, input().split()))
yy = list(map(int, input().split()))
for i in range(x+1, y+1):
    if max(xx) < i <= min(yy):
        print('No War')
        exit()
print('War')
