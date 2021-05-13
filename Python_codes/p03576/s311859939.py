def solve():
    res = float('inf')
    for i in range(n):
        r_top = coordinates[i][1]
        for j in range(n):
            r_bottom = coordinates[j][1]
            if r_bottom < r_top:
                continue
            for k in range(n):
                c_left = coordinates[k][0]
                for l in range(n):
                    c_right = coordinates[l][0]
                    if c_right < c_left:
                        continue
                    cnt = 0
                    for c, r in coordinates:
                        # print(r_top, r, r_bottom, c_left, c, c_right)
                        if (r_top <= r <= r_bottom) and (c_left <= c <= c_right):
                            cnt += 1
                            if cnt >= need:
                                res = min(res, (r_bottom - r_top) * (c_right - c_left))
                                break

    return res


n, need = map(int, input().split())
coordinates = tuple(sorted(tuple(map(int, input().split())) for _ in range(n)))
# x,y昇順

# print(coordinates)

print(solve())
