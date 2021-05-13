N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]
vec_dic = {}

max_same = 0
for i in range(N):
    x1,y1 = points[i]
    for j in range(N):
        if i == j:
            continue
        x2,y2 = points[j]
        d_x = x2 - x1
        d_y = y2 - y1
        if d_x in vec_dic.keys():
            if d_y in vec_dic[d_x].keys():
                vec_dic[d_x][d_y] += 1
                max_same = max(max_same, vec_dic[d_x][d_y])
            else:
                vec_dic[d_x][d_y] = 1
                max_same = max(max_same,1)
        else:
            vec_dic[d_x] = {d_y: 1}
            max_same = max(max_same, 1)
print(N-max_same)