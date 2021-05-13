import bisect


def main():
    n = int(input())
    a = [int(v) for v in input().split()]
    count = {}
    for i, v in enumerate(a):
        v = i - v
        if count.get(v) is None:
            count[v] = [i]
        else:
            count[v].append(i)

    ans = 0
    for i, v in enumerate(a):
        t = count.get(v+i)
        if t is None:
            continue
        idx = bisect.bisect_right(t, i)
        ans += len(t) - idx

    print(ans)


if __name__ == '__main__':
    main()
