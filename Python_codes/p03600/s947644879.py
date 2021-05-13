def main():
    from heapq import heappush, heappop

    n = int(input())
    a = [[int(x) for x in input().split()] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if a[i][j] != min(a[i][k] + a[k][j] for k in range(n)):
                print(-1)
                return

    h = []
    for r, row in enumerate(a):
        for c, cell in enumerate(row):
            if r == c: break
            heappush(h, (cell, r, c))  # dist,r,c

    pathes = []
    while h:
        dist, r, c = heappop(h)

        is_path = True
        for k in range(n):
            if k == r or k == c: continue
            if dist >= a[r][k] + a[k][c]:
                is_path = False
                break

        if is_path:
            pathes.append(dist)

    print(sum(pathes))


if __name__ == '__main__':
    main()
