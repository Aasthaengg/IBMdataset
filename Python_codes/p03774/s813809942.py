n, m = map(int, input().split())

student = list()

for x in range(n):
    student.append(list(map(int, input().split())))

checkpoint = list()

for y in range(m):
    checkpoint.append(list(map(int, input().split())))

INF = 4*(10**8) + 1
tmp = INF
ans = 51

for x in range(n):
    for y in range(m-1, -1, -1):
        distance = abs(student[x][0] - checkpoint[y][0]) + \
            abs(student[x][1] - checkpoint[y][1])

        if tmp >= distance:
            tmp = distance
            ans = y
    print(ans+1)
    tmp = INF
