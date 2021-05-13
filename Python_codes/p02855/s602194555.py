def get_h_list(S):
    H = len(S)
    n_offset_rows = 0
    while '#' not in S[n_offset_rows]:
        n_offset_rows += 1
    assert n_offset_rows < H
    h_list = list()
    for h in range(n_offset_rows, H):
        if '#' in S[h]:
            h_list.append(h)
    h_list[0] = 0
    h_list.append(H)
    return h_list


def get_w_list(S, h_from, h_to):
    W = len(S[0])
    n_offset_columns = 0
    while '#' not in [S[h][n_offset_columns] for h in range(h_from, h_to + 1)]:
        n_offset_columns += 1
    assert n_offset_columns < W
    w_list = list()
    for w in range(n_offset_columns, W):
        if '#' in [S[h][w] for h in range(h_from, h_to + 1)]:
            w_list.append(w)
    w_list[0] = 0
    w_list.append(W)
    return w_list


def main():
    H, W, K = map(int, input().split())
    ans = [[0 for _ in range(W)] for _ in range(H)]
    color = 1
    S = [input() for _ in range(H)]
    h_list = get_h_list(S)
    for i in range(len(h_list) - 1):
        h_from, h_to = h_list[i], h_list[i + 1] - 1
        w_list = get_w_list(S, h_from, h_to)
        for j in range(len(w_list) - 1):
            w_from, w_to = w_list[j], w_list[j + 1] - 1
            # 塗る
            for h in range(h_from, h_to + 1):
                for w in range(w_from, w_to + 1):
                    ans[h][w] = color
            color += 1
    for a in ans:
        print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()