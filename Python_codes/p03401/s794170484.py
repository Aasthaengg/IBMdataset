def main():
    m, *a = map(int, open(0).read().split())
    a = [0] + a + [0]
    s = 0
    p = [abs(i - j) for i, j in zip(a, a[1:])]
    s = sum(p)
    t = [str(s - abs(i - j) - abs(j - k) + abs(k - i)) for i, j, k in zip(a, a[1:], a[2:])]
    ans = "\n".join(t)
    print(ans)


if __name__ == '__main__':
    main()
