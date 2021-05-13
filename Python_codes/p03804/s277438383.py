n,m = map(int,input().split())
big_image_ls = [0] * n
small_image_ls = [0] * m
for i in range(n):
    a = input()
    big_image_ls[i] = a
for i in range(m):
    b = input()
    small_image_ls[i] = b

diff = n-m+1
include = False
for up_y in range(diff):
    for left_x in range(diff):
        same = True
        for y in range(up_y, up_y+m):
            for x in range(left_x,left_x+m):
                if small_image_ls[y-up_y][x-left_x] != big_image_ls[y][x]:
                    same = False
        if same:
            include = True
if include:
    print('Yes')
else:
    print('No')
            



