if __name__ == '__main__':
    n = int(input())
    s = list(input())
    all_b = s.count("#")
    all_w = s.count(".")

    b = [0 for i in range(n)]
    w = [0 for i in range(n)]

    if s[0] == "#":
        b[0] = 1
    else:
        w[0] = 1
    for i in range(1, n):
        if s[i] == "#":
            b[i] = b[i - 1] + 1
            w[i] = w[i - 1]
        else:
            b[i] = b[i - 1]
            w[i] = w[i - 1] + 1

    ans = min(all_w, all_b)
    for i in range(n):
        ans = min(ans, b[i] + (all_w - w[i]))
    print(ans)
