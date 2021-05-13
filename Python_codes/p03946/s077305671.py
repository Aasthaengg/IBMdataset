def slove():
    import sys
    import collections
    input = sys.stdin.readline
    n, t = list(map(int, input().rstrip('\n').split()))
    a = list(map(int, input().rstrip('\n').split()))
    d = collections.defaultdict(list)
    m = 10 ** 10
    for v in a:
        if v < m:
            m = v
        else:
            d[v-m] += [m]
    d = sorted(d.items(), key=lambda x: x[0], reverse=True)
    print(len(d[0][1]))


if __name__ == '__main__':
    slove()
