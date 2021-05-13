def main():
    import sys
    from collections import Counter
    # readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    H, W, N = map(int, input().split())
    P = set()
    for s in readlines():
        a, b = map(int, s.split())
        a -= 1; b -= 1
        P.add((a, b))

    cnt = Counter()
    for a, b in P:
        for oa in range(a - 2, a + 1):
            for ob in range(b - 2, b + 1):
                if 0 <= oa <= H - 3 and 0 <= ob <= W - 3:
                    cnt[(oa, ob)] += 1
    ans = Counter(cnt.values())
    ans[0] = (H - 2) * (W - 2) - sum(ans.values())

    for i in range(10):
        print(ans[i])


if __name__ == "__main__":
    main()
