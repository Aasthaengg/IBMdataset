def main():
    DIFF = 400

    N = int(input())

    ctr = [0] * 9
    for x in map(int, input().split()):
        ctr[min(x // DIFF, 8)] += 1

    le_red = sum(c > 0 for c in ctr[:8])
    gt_red = ctr[8]

    if gt_red:
        if le_red:
            print(le_red, le_red + gt_red)
        else:
            print(1, gt_red)
    else:
        print(le_red, le_red)


if __name__ == '__main__':
    main()
