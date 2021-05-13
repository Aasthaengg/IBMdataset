if __name__ == "__main__":
    INF = 40 ** 18 + 1
    N, K = map(int, input().split())
    Point = list()
    for i in range(N):
        Point.append(list(map(int, input().split())))

    # 四角形の頂点を２点選んでその中にK点含まれてて、面積が小さければ更新
    ans = INF
    # iは1点目のx, jは1点目のy、kは2点目のx, lは2点目のy
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    x0 = Point[i][0]
                    y0 = Point[j][1]
                    x1 = Point[k][0]
                    y1 = Point[l][1]
                    # 四角形作れない座標の組み合わせと、1点目 < 2点目の座標関係で無いならスルー
                    if x0 >= x1 or y0 >= y1:
                        continue
                    count = 0
                    for m in range(N):
                        x, y = Point[m][0], Point[m][1]
                        if x0 <= x <= x1 and y0 <= y <= y1:
                            count += 1
                        if count >= K:
                            area = (x1 - x0) * (y1 - y0)
                            if area < ans:
                                ans = area
                            break

    print(ans)
