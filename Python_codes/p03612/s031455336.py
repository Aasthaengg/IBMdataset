def main():
    N = int(input())
    P = list(map(int, input().split(' ')))
    flags = [1 if i + 1 == p else 0 for i, p in enumerate(P)]
    seq_nums = list()
    n = 0
    for f in flags:
        if f == 1:
            n += 1
        elif n > 0:
            seq_nums.append(n)
            n = 0
    if n > 0:
        seq_nums.append(n)
    print(sum([(s - 1) // 2 + 1 for s in seq_nums]))


if __name__ == '__main__':
    main()