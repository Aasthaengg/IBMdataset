def main():
    X = input()
    cnt_s = 0
    cnt_removal = 0
    for x in X:
        if x == 'T':
            if cnt_s > 0:
                cnt_s -= 1
                cnt_removal += 1
        else:
            cnt_s += 1
    print(len(X) - 2 * cnt_removal)


if __name__ == '__main__':
    main()