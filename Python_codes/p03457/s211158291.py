n = int(input())

infos = [[0,0,0]]
for i in range(n):
    infos.append(list(map(int,input().split())))

for i in range(n):
    t = infos[i+1][0]-infos[i][0]
    abs_x = abs(infos[i][1]-infos[i+1][1])
    abs_y = abs(infos[i][2]-infos[i+1][2])
    d = abs_x + abs_y
    if t < d or t%2!=d%2:
        print("No")
        exit()

print("Yes")