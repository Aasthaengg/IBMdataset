def main():
    S = input()
    smaller_cnt = [0]  # <
    seq_cnt = 0
    for c in S:
        if c != '<':
            seq_cnt = 0
        else:
            seq_cnt += 1
        smaller_cnt.append(seq_cnt)
    larger_cnt = [0]  # >
    for c in S[::-1]:
        if c != '>':
            seq_cnt = 0
        else:
            seq_cnt += 1
        larger_cnt.append(seq_cnt)
    larger_cnt.reverse()
    ans = 0
    for x, y in zip(smaller_cnt, larger_cnt):
        ans += max([x, y])
    print(ans)


if __name__ == '__main__':
    main()