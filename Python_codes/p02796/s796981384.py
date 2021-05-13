def main():
    N, *XL = map(int, open(0).read().split())
    # print(N, XL)
    robots = [0]*N
    for i in range(N):
        X, L = XL[2 * i + 0], XL[2 * i + 1]
        robots[i] = (X - L, X + L)
    robots.sort(key=lambda x: x[1])
    # print(robots)
    ans = 0
    last = robots[0][0] - 1
    for robot in robots:
        if last <= robot[0]:
            last = robot[1]
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
