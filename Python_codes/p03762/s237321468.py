def main():
    n, m = map(int, input().split())
    mod = pow(10, 9) + 7
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    prefix_x = [0]
    prefix_y = [0]
    for i in range(n):
        prefix_x.append(prefix_x[-1] + x[i])
    for i in range(m):
        prefix_y.append(prefix_y[-1] + y[i])

    # print(prefix_x)
    # print(prefix_y)
    ysum = 0
    for j in range(1, m):
        ysum += j*y[j] - prefix_y[j]
        ysum %= mod
    xsum = 0
    for j in range(1, n):
        xsum += j*x[j] - prefix_x[j]
        xsum %= mod

    # print(xsum)
    # print(ysum)
    return ysum * xsum % mod


if __name__ == '__main__':
    print(main())
