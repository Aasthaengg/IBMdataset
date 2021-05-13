n, k, q = map(int, input().split())

points = [0] * n

for i in range(q):
    points[int(input()) - 1] += 1

for point in points:
    if(point > q - k):
        print("Yes")
    else:
        print("No")