N, C = map(int, input().split())
X_V = [list(map(int, input().split())) for i in range(N)]
max_en = 0
point = [0] * (N+1)
point_back = [0] * (N+1)
point_rev = [0] * (N+1)
point_rev_back = [0] * (N+1)
max_point = [0] * (N+1)
max_point_back = [0] * (N+1)
max_point_rev = [0] * (N+1)
max_point_rev_back = [0] * (N+1)
for i, x_v in enumerate(X_V):
    # print(X_V[N-i-1])
    if i == 0:
        point[i+1] = x_v[1] - x_v[0]
        point_back[i+1] = x_v[1] - x_v[0]*2
        point_rev[i+1] = X_V[N-i-1][1] - (C-X_V[N-i-1][0])
        point_rev_back[i+1] = X_V[N-i-1][1] - (C-X_V[N-i-1][0])*2
    else:
        point[i+1] = point[i]+x_v[1] - (x_v[0]-X_V[i - 1][0])
        point_back[i+1] = point[i+1] - x_v[0]
        point_rev[i+1] = point_rev[i]+X_V[N-i-1][1] - (X_V[N-i][0]-X_V[N-i-1][0])
        point_rev_back[i+1] = point_rev[i+1] - (C-X_V[N-i-1][0])

    max_point[i + 1] = max(max_point[i], point[i + 1])
    max_point_back[i + 1] = max(max_point_back[i], point_back[i + 1])
    max_point_rev[i + 1] = max(max_point_rev[i], point_rev[i + 1])
    max_point_rev_back[i + 1] = max(max_point_rev_back[i],
                                    point_rev_back[i + 1])

# print(point)
# print(point_back)
# print(point_rev)
# print(point_rev_back)
for i in range(N+1):
    # print(i, N-i)
    max_en = max(max_en, max_point[i], max_point_rev[N-i], max_point_back[i] + max_point_rev[N-i],
                 max_point[i] + max_point_rev_back[N-i])
    # for j in range(N+1):
    #     if i + j > N:
    #         break
    #     else:
    #         if j == 0:
    #             max_en = max(max_en, point[i])
    #             # print(i, j, point[i])
    #         elif i == 0:
    #             max_en = max(max_en, point_rev[j])
    #             # print(i, j, point_rev[j])
    #         else:
    #             max_en = max(max_en, point_back[i] + point_rev[j], point[i] + point_rev_back[j])
    #             # print(i, j, point_back[i] + point_rev_back[j])

print(max_en)