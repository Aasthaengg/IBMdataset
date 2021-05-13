import sys

n, x, y = map(int, input().split())
x -= 1
y -= 1

def calc(i, j, x, y):
    mindist = abs(j - i)
    mindist = min(mindist, abs(x - i) + 1 + abs(y - j))
    mindist = min(mindist, abs(y - i) + 1 + abs(x - j))
    return mindist

result = [0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j :
            continue
        k = calc(i, j, x, y)       
        result[k] += 1

for i in range(1, n):
    print(result[i] // 2)