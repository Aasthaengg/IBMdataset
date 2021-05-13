def main():
    x, y, a, b, c = map(int, input().split())
    p = sorted([int(v) for v in input().split()])[-x:]
    q = sorted([int(v) for v in input().split()])[-y:]
    r = [int(v) for v in input().split()]
    r.extend(p)
    r.extend(q)
    print(sum(sorted(r)[-(x+y):]))


if __name__ == '__main__':
    main()
