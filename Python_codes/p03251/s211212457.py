n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
flag = False
if x[-1] < y[0]:
    for i in range(x[-1], y[0]+1):
        if i == x[-1]:
            if X <= i < Y:
                flag = True
                break
        elif i == y[0]:
            if X < i <= Y:
                flag = True
                break
        else:
            if X < i < Y:
                flag = True
                break
if flag:
    print("No War")
else:
    print("War")