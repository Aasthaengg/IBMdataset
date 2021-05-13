points = {}
n = int(input())
for _ in range(n):
    s = input()
    points.setdefault(s, 0)
    points[s] += 1
m = int(input())
for _ in range(m):
    s = input()
    points.setdefault(s, 0)
    points[s] -= 1
print(max(0, max(points.values())))