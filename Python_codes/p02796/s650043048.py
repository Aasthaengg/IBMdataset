n = int(input())

robot_list = []

for i in range(n):
    x, l = list(map(int, input().split()))
    robot_list.append([x+l, x-l, l])

delete_robot = 0
robot_list.sort()
temp_robot = robot_list[0]

for i in range(n-1):
    if temp_robot[0] > robot_list[i+1][1]:
        delete_robot += 1
    else:
        temp_robot = robot_list[i+1]

print(n - delete_robot)
