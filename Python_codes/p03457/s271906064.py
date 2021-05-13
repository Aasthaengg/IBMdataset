N = int(input())
TXY = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    TXY[i] = list(map(int, input().split()))

start = 0
start_x = 0
start_y = 0
for i in range(N):
    time = TXY[i][0] - start
    walk = [0 for _ in range(time)]
    diff_x = TXY[i][1] - start_x
    diff_y = TXY[i][2] - start_y
    total = len(walk) - (abs(diff_x) + abs(diff_y))
    if total < 0:
        print("No")
        exit()
    else:
        if total % 2 != 0:
            print(("No"))
            exit()
    start = TXY[i][0]
    start_x = TXY[i][1]
    start_y = TXY[i][2]
print("Yes")
