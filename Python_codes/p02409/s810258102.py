rooms = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())
for l in range(n):
    a,b,c,d = map(int, input().split())
    rooms[a-1][b-1][c-1] += d
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(" " + str(rooms[i][j][k]), end = "")
        print()
    if i != 3:
        print("####################")
