def main():
    n, *a = map(int, open(0).read().split())
    x1 = sum(a[::2]) - sum(a[1::2])
    x = [x1]
    for i in a[:-1]:
        x.append(2 * i - x[-1])
    ans = ' '.join(map(str, x))
    print(ans)


if __name__ == '__main__':
    main()
