def main():
    H, W, D = list(map(int, input().split(' ')))
    cell_list = list()
    for h in range(H):
        a_list = list(map(int, input().split(' ')))
        cell_list.extend([(a - 1, h, w) for w, a in enumerate(a_list)])
    cell_list.sort(key=lambda c: c[0])  # sort by cell number
    # calculate cumulative sum of magical power
    cumsum = dict()
    for d in range(D):
        cumsum[d] = [0]
    for x in range(D, H * W):
        d = x % D
        bef_c, c = cell_list[x - D], cell_list[x]
        m = cumsum[d][-1] + abs(c[1] - bef_c[1]) + abs(c[2] - bef_c[2])
        cumsum[d].append(m)
    # answer queries
    Q = int(input())
    queries = [list(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(Q)]
    for L, R in queries:
        d = L % D
        print(cumsum[d][R // D] - cumsum[d][L // D])


if __name__ == '__main__':
    main()