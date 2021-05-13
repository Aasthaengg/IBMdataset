from itertools import product


def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10**4
    for p in product(range(4), repeat=n):
        abc = [[], [], []]
        for i, pi in enumerate(p):
            if pi > 0:
                abc[pi - 1].append(i)
        fl = False
        for i in abc:
            fl |= len(i) == 0
        if fl:
            continue
        cost = 0
        for i in range(3):
            cost += abs(sum(l[j] for j in abc[i]) - (a, b, c)[i]) + 10 * (len(abc[i]) - 1)
        ans = min(ans, cost)
    print(ans)


if __name__ == '__main__':
    main()
