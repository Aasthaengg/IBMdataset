X, Y = map(int, input().split())
if X % Y == 0:
    print(-1)
    exit()
for i in range(10**9 // X + 1):
    Xi = X * i
    if Xi % Y != 0:
        print(Xi)
        exit()
print(-1)
