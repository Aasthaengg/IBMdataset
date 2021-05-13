n, m, x, y = map(int, input().split())
if x>y :
    print('War')
else  :
    X = sorted(list(map(int, input().split())))
    Y = sorted(list(map(int, input().split())))
    a = 0
    for i in range(x+1, y+1):
        if X[-1]<i and i <= Y[0] and x < i and i <= y:
            print('No War')
            break
        else :
            a += 1
    if a == y-x:
        print('War')
