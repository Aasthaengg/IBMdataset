def main():
    import collections

    n = int(input())
    s = list(input())

    cnt_s = []

    for i in range(n):
        cnt_l = collections.Counter(s[:i])
        cnt_r = collections.Counter(s[i:])
        cnt = 0
        for key in dict(collections.Counter(cnt_l)):
            if key in dict(collections.Counter(cnt_r)):
                cnt += 1
        cnt_s.append(cnt)

    print(max(cnt_s))


if __name__ == '__main__':
    main()