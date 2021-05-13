def warshall_floyd(v_count: int, matrix: list) -> list:
    """ ワーシャルフロイド
    v_count: 頂点数
    matrix: 隣接行列(到達不能はfloat("inf"))
    """
    for i in range(v_count):
        for j, c2 in enumerate(row[i] for row in matrix):
            for k, (c1, c3) in enumerate(zip(matrix[j], matrix[i])):
                if c1 > c2+c3:
                    matrix[j][k] = c2+c3
    return matrix


h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
warshall_floyd(10, c)
ans = 0
for _ in range(h):
    for x in list(map(int, input().split())):
        if x >= 0:
            ans += c[x][1]
print(ans)
