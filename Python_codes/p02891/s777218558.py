if __name__ == '__main__':
    s = list(input())
    ss = s + s
    k = int(input())
    if len(set(s)) == 1:
        print(len(s) * k // 2)
        exit(0)

    tmp, tmp2 = 0, 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            tmp += 1
            s[i + 1] = '-1'
    for i in range(len(s) * 2 - 1):
        if ss[i] == ss[i + 1]:
            tmp2 += 1
            ss[i + 1] = '-1'
    print(tmp + (tmp2 - tmp) * (k - 1))
