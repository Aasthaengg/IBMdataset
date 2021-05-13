def solve(m, bs):
    ans = 0
    x_y_z = 0

    for i in range(1 << 3):
        xyzs = []
        for b in bs:
            for j in range(3):
                if i >> j & 1:
                    x_y_z += b[j]
                else:
                    x_y_z -= b[j]
            xyzs.append(x_y_z)
            x_y_z = 0

        xyzs.sort(reverse=True)
        s_xyzs = sum(xyzs[:m])
        ans = s_xyzs if s_xyzs > ans else ans

    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    x, y, z = 0, 0, 0
    bs = []

    for i in range(n):
        x, y, z = map(int, input().split())
        bs.append([x, y, z])

    print(solve(m, bs))
