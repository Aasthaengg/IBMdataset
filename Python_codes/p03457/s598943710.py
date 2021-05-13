from sys import exit

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

l.insert(0, [0, 0, 0])
for i in range(n):
    t1, x1, y1 = l[i]
    t2, x2, y2 = l[i+1]
    d = abs(x2 - x1) + abs(y2 - y1)
    t = t2 - t1
    if d > t or (d + t) % 2 == 1:
        print('No')
        exit()

print('Yes')