X, Y = map(int, input().split())

flag = True
for i in range(1, 10 ** 6):
    if X * i % Y != 0:
        print(X * i)
        flag = False
        break

if flag:
    print(-1)