def dissatisfy(c, last, d, v):
    ans = 0
    for i in range(0, 26):
        if (i != v - 1):
            ans += c[i] * (d - last[i])
    return ans


def main():
    D = int(input())
    c = list(map(int, input().split()))
    last = [0] * 27
    s = list()
    ans = 0

    for d in range(0, D):
        s.append(list(map(int, input().split())))
    for d in range(1, D + 1):
        v = int(input())
        ans += s[d-1][v-1]
        ans -= dissatisfy(c, last, d, v)
        for j in range(0, 27):
            if j == v - 1:
                last[j] = d
        print(ans)


if __name__ == '__main__':
    main()
