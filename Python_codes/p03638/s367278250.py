def main():
    h, w, n, *a = map(int, open(0).read().split())
    s = sum([[i + 1] * a[i] for i in range(n)], [])

    for i in range(h):
        print(' '.join(map(str, s[i * w:(i + 1) * w])) if i % 2 == 0 else ' '.join(map(str, s[i * w:(i + 1) * w][::-1])))


if __name__ == '__main__':
    main()
