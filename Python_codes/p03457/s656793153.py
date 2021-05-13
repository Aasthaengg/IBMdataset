N = int(input())
L = [list(map(int, input().split())) for i in range(N)]

l = [[0, 0, 0]]
l.extend(L)

flag = True
for c in range(1, len(l)):
    dt = l[c][0] - l[c-1][0]
    dist = abs(l[c][1] - l[c-1][1]) + abs(l[c][2] - l[c-1][2])

    if dist > dt or (dist % 2) != (dt % 2):
        flag = False

print("Yes" if flag else "No")
