def resolve():
    N, Cnum = list(map(int, input().split()))
    D = [list(map(int, input().split())) for _ in range(Cnum)]
    C = [list(map(int, input().split())) for _ in range(N)]
    color_count = [{}, {}, {}]
    for i in range(N):
        for j in range(N):
            group = (i+j)%3
            d = color_count[group]
            if C[i][j]-1 in d:
                d[C[i][j]-1] += 1
            else:
                d[C[i][j]-1] = 1
    
    ans = float("inf")
    import itertools
    for pattern in itertools.permutations(list(range(0, Cnum)), 3):
        total = 0
        for i, after in enumerate(pattern):
            for color, count in color_count[i].items():
                total += count*D[color][after]
        ans = min(ans, total)
    print(ans)

if '__main__' == __name__:
    resolve()