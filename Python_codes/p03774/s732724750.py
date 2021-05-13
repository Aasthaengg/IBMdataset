n, m = map(int, input().split())
student = [list(map(int, input().split())) for _ in range(n)]
check = [list(map(int, input().split())) for _ in range(m)]

for a, b in student:
    pos = 0
    dis = 10**9
    for i, x in enumerate(check, 1):
        c, d = x
        mdis = abs(a-c) + abs(b - d)
        if mdis < dis:
            pos = i
            dis = mdis
    print(pos)
