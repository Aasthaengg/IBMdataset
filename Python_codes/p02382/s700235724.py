import math

dim = int(input().strip())
vec_x = list(map(int,input().strip().split(" ")))
vec_y = list(map(int,input().strip().split(" ")))

dist_1 = 0
dist_2 = 0
tmp_dist_2 = 0
dist_3 = 0
tmp_dist_3 = 0
dist_infinite = 0
abs_xy = [0 for i in range(dim)]
for i in range(dim):
    abs_xy[i]= abs(vec_x[i]-vec_y[i])
    
    dist_1 = dist_1 + abs_xy[i]
    tmp_dist_2 = tmp_dist_2 + abs_xy[i] ** 2
    tmp_dist_3 = tmp_dist_3 + abs_xy[i] ** 3
    
dist_2 = math.sqrt(tmp_dist_2)
dist_3 = tmp_dist_3 ** (1/3)
dist_infinite = max(abs_xy)

print("{:.5f}\n{:.5f}\n{:.5f}\n{:.5f}".format(dist_1,dist_2,dist_3,dist_infinite))