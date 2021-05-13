n, m, xx, yy = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.append(xx)
y.append(yy)
if min(y) - max(x) > 0:
    print('No War')
else:
    print('War')