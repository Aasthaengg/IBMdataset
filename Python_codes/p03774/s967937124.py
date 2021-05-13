n, m = list(map(int, input().split()))
s = []
c = []

for i in range(n):
    s.append(list(map(int, input().split())))

for i in range(m):
    c.append(list(map(int, input().split())))

for student in s:
    index = 1000
    idist = 1e9

    for i in range(m):
        dist = abs(student[0] - c[i][0]) + abs(student[1] - c[i][1])
        if (dist < idist):
            idist = dist
            index = i

    print(index + 1)