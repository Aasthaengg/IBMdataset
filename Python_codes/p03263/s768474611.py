def main():
    h, w, *a = map(int, open(0).read().split())

    cnt = 0
    ans = ''
    for k in range(h * w):
        i, j = divmod(k, w)

        if a[k] % 2 == 0:
            continue
        if j != w - 1:
            cnt += 1
            a[k + 1] += 1
            ans += '{0} {1} {2} {3}\n'.format(i + 1, j + 1, i + 1, j + 2)
        elif i != h - 1:
            cnt += 1
            a[k + w] += 1
            ans += '{0} {1} {2} {3}\n'.format(i + +2, j + 1, i + 1, j + 1)
        else:
            pass
    print(cnt)
    print(ans)


if __name__ == '__main__':
    main()
