N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
x = sorted(x, reverse=True)[0]
y = list(map(int, input().split()))
y = sorted(y)[0]


for z in range(-100, 101):
    if X < z <= Y and z <= y and x < z:
        print('No War')
        break
else:
    print('War')
