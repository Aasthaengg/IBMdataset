def main():
    N, K = map(int, input().split())

    edges = []
    for u in range(1, N):
        edges.append((0, u))

    count = (N - 1) * (N - 2) // 2
    to_join = count - K

    v = 1
    while v < N and to_join:
        for u in range(v + 1, N):
            edges.append((v, u))
            to_join -= 1
            if to_join == 0: break
        v += 1

    if to_join:
        print(-1)
    else:
        print(len(edges))
        for edge in edges:
            print(*map(lambda x: x + 1, edge))


if __name__ == '__main__':
    main()

# 中心0を取り囲む
# (n-1)個の頂点
# (n-1)C2の最短距離2の組が存在
# (n-1)個の頂点同士の組のいくつかを直接連結すると最短距離1にできる
