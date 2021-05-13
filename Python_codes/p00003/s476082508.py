data = []
n = int(input())
for i in range(n):
    data.append(list(map(int, input().split())))
    data[i] = sorted(data[i])[::-1]

for j in range(n):
    if data[j][0]**2 == data[j][1]**2 + data[j][2]**2:
        print('YES')
    else:
        print('NO')