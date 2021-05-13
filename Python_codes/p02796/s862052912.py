n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]
robot = []

for v in xl:
    robot.append([v[0]-v[1], v[0]+v[1]])
robot.sort(key=lambda x:x[1])

prev = 0
cnt = 0
for i in range(1, n):
    if robot[prev][1] > robot[i][0]:
        cnt += 1
    else:
        prev = i
print(n-cnt)