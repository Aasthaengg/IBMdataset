N = int(input())
txy = [list(map(int, input().split())) for i in range(N)]
stxy = sorted(txy, key=lambda x:(x[0]))

stxy.insert(0, [0, 0, 0])

for i in range(1, N+1):
    if stxy[i][0] - stxy[i-1][0] < abs(stxy[i][1]-stxy[i-1][1]) + abs(stxy[i][2]-stxy[i-1][2]):
        print("No")
        exit()
    elif (stxy[i][0] - stxy[i-1][0] - (abs(stxy[i][1]-stxy[i-1][1]) + abs(stxy[i][2]-stxy[i-1][2])))%2 == 1:
        print("No")
        exit()

print("Yes")
