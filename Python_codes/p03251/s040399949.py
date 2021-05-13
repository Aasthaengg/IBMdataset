N, M, X, Y = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
xs.sort()
ys.sort()
for z in range(X + 1, Y + 1):
    if xs[-1] < z <= ys[0]:
        print('No War')
        break
else:
    print('War')