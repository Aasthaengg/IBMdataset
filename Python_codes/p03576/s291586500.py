def main():
    n,k = map(int,input().split())
    xy = [list(map(int,input().split())) for _ in range(n)]

    ans = 10 ** 20

    for i in range(n):
        for j in range(i+1, n):
            for ii in range(n):
                for jj in range(ii+1, n):
                    l = min(xy[i][0], xy[j][0])
                    r = max(xy[i][0], xy[j][0])
                    d = min(xy[ii][1], xy[jj][1])
                    u = max(xy[ii][1], xy[jj][1])
                    cnt = 0
                    for x,y in xy:
                        if l <= x <= r and d <= y <= u:
                            cnt += 1
                    if cnt >= k:
                        ans = min(ans, (r-l) * (u - d))

    print(ans)

if __name__ == '__main__':
    main()
