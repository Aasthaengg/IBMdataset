def main():
    N, C = (int(i) for i in input().split())
    D = [[int(i) for i in input().split()] for j in range(C)]
    c = [[int(i) for i in input().split()] for j in range(N)]
    base = [[((i+1)+(j+1)) % 3 for j in range(N)] for i in range(N)]
    d = [{i: 0 for i in range(1, C + 1)} for j in range(3)]
    for i in range(N):
        for j in range(N):
            d[base[i][j]][c[i][j]] += 1

    ans = 1 << 60
    from itertools import combinations, permutations
    for comb in combinations(range(1, C+1), 3):
        for p in permutations(comb):
            cur = 0
            for i in range(3):
                for k, v in d[i].items():
                    cur += D[k-1][p[i]-1] * v
            ans = min(ans, cur)
    print(ans)


if __name__ == '__main__':
    main()
