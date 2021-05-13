def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    x, y = [0]*n, [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    from collections import defaultdict
    xy = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            xy[(x[i]-x[j], y[i]-y[j])] += 1
    if xy == {}:
        print(1)
        return
    p, q = max(xy, key=lambda x: xy[x])
    ans = n
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if x[i]-x[j] == p and y[i]-y[j] == q:
                ans -= 1
    print(ans)


if __name__ == '__main__':
    main()