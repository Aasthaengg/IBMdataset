N = int(input())
T = []
X = []
Y = []
for _ in range(N):
    t,x,y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

before_t = before_x = before_y = 0

for t,x,y in zip(T,X,Y):

    if before_t == 0:
        if t != x + y:
            print('No')
            exit()

    d = abs(x + y - before_x - before_y)

    if t - before_t >= d:
        if (t - before_t) % 2 == 0 and d % 2 == 0:
            pass
        elif (t - before_t) % 2 != 0 and d % 2 != 0:
            pass
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()

    before_t = t
    before_x = x
    before_y = y

else:
    print('Yes')