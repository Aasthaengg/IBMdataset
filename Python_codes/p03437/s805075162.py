X, Y = map(int, input().split())
if X % Y == 0:
    print(-1)
    exit()

# for i in range(int(1e9), 0, -1):
for i in range(1, int(1e9)):
    if X * i % Y != 0:
        print(X * i)
        exit()
print(-1)
