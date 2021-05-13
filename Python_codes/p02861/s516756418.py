import math

n = int(input())
d = [[0] * n for _ in range(n)]
p = []
for i in range(n):
    p.append(tuple(map(int, input().split())))

s = 0
for i in range(n):
    xi, yi = p[i]
    for j in range(i+1, n):
        xj, yj = p[j]
        s += math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
s = s * 2 / n
print(s)