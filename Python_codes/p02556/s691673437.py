n = int(input())
point_dict1 = {}
point_dict2 = {}
for i in range(n):
    x, y = map(int, input().split())
    point_dict1[x + y] = (x, y)
    point_dict2[y - x] = (x, y)
min_point1 = min(point_dict1)
max_point1 = max(point_dict1)
min_point2 = min(point_dict2)
max_point2 = max(point_dict2)
print(max(max_point1 - min_point1, max_point2 - min_point2))