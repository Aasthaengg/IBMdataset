def main():
    h, w, *a = map(int, open(0).read().split())
    m = [a[i * w:(i + 1) * w] for i in range(h)]
    m.append([2] * w)

    ans = ''
    cnt = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] % 2 == 0:
                continue
            if j != w - 1:
                cnt += 1
                m[i][j + 1] += 1
                ans += '{0} {1} {2} {3}\n'.format(i + 1, j + 1, i + 1, j + 2)
            elif i != h - 1:
                cnt += 1
                m[i + 1][j] += 1
                ans += '{0} {1} {2} {3}\n'.format(i + +2, j + 1, i + 1, j + 1)
            else:
                pass
    print(cnt)
    print(ans)


if __name__ == '__main__':
    main()
