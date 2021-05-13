def main():
    n, *b = map(int, open(0).read().split())

    m = []
    for k in range(1, n + 1):
        for i in range(n - k, -1, -1):
            if b[i] == i + 1:
                b.pop(i)
                m.append(i + 1)
                break
        else:
            print(-1)
            exit()

    print('\n'.join(map(str, m[::-1])))


if __name__ == '__main__':
    main()
