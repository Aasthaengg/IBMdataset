n = int(input())
points = list(map(int, input().split()))

points.sort()
start = points[0]
cnt = 0
for i in points:
    cnt += i -start
    start = i

print(cnt)