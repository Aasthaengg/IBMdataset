def main():
    from collections import defaultdict
    n, *a = map(int, open(0).read().split())
    d = defaultdict(lambda: {'R': 0, 'L': 0})

    for i, x in enumerate(a, 1):
        d[i + x]['R'] += 1
        d[i - x]['L'] += 1

    ans = 0
    for key, dic in d.items():
        l = dic['L']
        r = dic['R']
        ans += l * r

    print(ans)


if __name__ == '__main__':
    main()
