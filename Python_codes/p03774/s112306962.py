from sys import stdin
def input():
    return stdin.readline().strip()

n, m = map(int, input().split())
a, b, c, d = [], [], [], []
for _ in range(n):
    i, j = map(int, input().split())
    a.append(i)
    b.append(j)
for _ in range(m):
    i, j = map(int, input().split())
    c.append(i)
    d.append(j)

l = []
for i in range(n):
    ans = (float('inf'), 0)
    for j in range(m):
        distance = (abs(a[i] - c[j]) + abs(b[i] - d[j]), j)
        if distance < ans:
            ans = distance
    l.append(ans[1] + 1)

for i in l:
    print(i)