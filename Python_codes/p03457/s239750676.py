n = int(input())
points = []
points.append([0, 0, 0])
can = True
for i in range(n):
    points.append([i for i in map(int, input().split())])
    move_n = points[i+1][0] - points[i][0]
    dist = abs(points[i+1][1] - points[i][1]) + abs(points[i+1][2] - points[i][2])
    if move_n < dist or dist % 2 != move_n % 2:
        can = False 
        break
# print(points)
# can = True
# for i in range(len(points)-1):
#     move_n = points[i+1][0] - points[i][0]
#     dist = abs(points[i+1][1] - points[i][1]) + abs(points[i+1][2] - points[i][2])
#     if move_n < dist or dist % 2 != move_n % 2:
#         can = False 
#         break

if can:
    print('Yes')
else:
    print('No')