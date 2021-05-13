X, Y = map(int, input().split())
if X % Y == 0:
    print(-1)
    exit(0)
for i in range(2, 10 ** 18):
    if X * i % Y != 0:
        print(X * i)
        exit(0)
