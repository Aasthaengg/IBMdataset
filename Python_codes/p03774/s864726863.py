n, m = map(int,input().split())
students = []
for _ in range(n):
    students.append(list(map(int,input().split())))
points = []
for _ in range(m):
    points.append(list(map(int,input().split())))

anslst = []
for i in range(n):
    distance = 10 ** 9
    num = -1
    for j in range(m):
        tmp = abs(students[i][0] - points[j][0]) + abs(students[i][1] - points[j][1])
        if tmp < distance:
            distance = tmp
            num = j + 1
    anslst.append(num)

for p in anslst:
    print(p)