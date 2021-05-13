n = int(input())
Restaurant = []
for i in range(n):
    cmd = input().split()
    Restaurant.append([i + 1, cmd[0], int(cmd[1])])
sorted_Restaurant = sorted(Restaurant, key=lambda x: (x[1], -x[2]))
for j in sorted_Restaurant:
    print(j[0])
