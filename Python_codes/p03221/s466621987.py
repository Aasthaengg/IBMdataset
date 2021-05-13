import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    results = {}
    p_list = []
    y_list = []
    cnt = 0
    for i in range(m):
        p, y = map(int, input().split())
        p_list.append(p)
        y_list.append(y)
        if results.get(p) is None:
            results[p] = [y]
        else:
            results[p].append(y)
    for i, p in results.items():
        p_sorted = sorted(p)
        results[i] = p_sorted

    for i, p in enumerate(p_list):
        import bisect
        print('{:006}'.format(p) + '{:006}'.format(bisect.bisect_left(results[p], y_list[i]) + 1))


if __name__ == "__main__":
    main()
