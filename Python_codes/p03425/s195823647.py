def main():
    N = int(input())
    A = [input()[0] for i in range(N)]
    from collections import Counter
    from itertools import combinations
    c = Counter(A)
    d = ('M', 'A', 'R', 'C', 'H')
    ans = 0
    for (a1, a2, a3) in combinations(d, 3):
        ans += c[a1] * c[a2] * c[a3]
    print(ans)


if __name__ == '__main__':
    main()
