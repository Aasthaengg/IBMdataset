def main():
    N = int(input())
    P = [int(input()) - 1 for _ in range(N)]
    indices = [0] * N
    for i, p in enumerate(P):
        indices[p] = i
    max_cnt = 0  # indexの値が単調増加になるような最長の列長
    cur_index, cur_cnt = -1, 0
    for p in range(N):
        index = indices[p]
        if index > cur_index:
            cur_cnt += 1
        else:
            max_cnt = max(max_cnt, cur_cnt)
            cur_cnt = 1
        cur_index = index
    max_cnt = max(max_cnt, cur_cnt)
    print(N - max_cnt)


if __name__ == '__main__':
    main()