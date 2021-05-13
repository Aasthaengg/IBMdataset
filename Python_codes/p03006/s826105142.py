def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    xy = []
    for _ in range(N):
        x, y = map(int, input().split())
        xy.append((x, y))

    d = {}
    for i in range(N):
        tmp = set()
        for j in range(N):
            if i == j:
                continue
            dx = xy[i][0] - xy[j][0]
            dy = xy[i][1] - xy[j][1]

            if (dx, dy) in tmp:
                continue
            if (dx, dy) not in d:
                d[(dx, dy)] = 1
            else:
                d[(dx, dy)] += 1
            tmp.add((dx, dy))

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    cnt = d[0][1]
    print(N - cnt)

main()