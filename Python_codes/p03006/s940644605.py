n = int(input())
balls = []
for i in range(n):
    x, y = map(int, input().split())
    balls.append((x, y))

dic = {}

for i in range(n):
    for j in range(n):
        if i != j:
            coordinate = str((balls[i][0] - balls[j][0], balls[i][1] - balls[j][1]))
            if coordinate in dic:
                dic[coordinate] += 1
            else:
                dic[coordinate] = 1

dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
if len(dic) == 0:
    print(n)
else:
    print(n - dic[0][1])
