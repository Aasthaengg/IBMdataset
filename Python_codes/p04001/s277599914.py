def main():
    S = input()
    n = len(S) - 1
    ans = 0

    if n == 0:
        print(int(S))
        return

    for i in range(2 ** n):
        plus_lst = [0] * n
        for j in range(n):
            if (i >> j) & 1 == 1:
                plus_lst[n - 1 - j] = 1  # 0: "", 1: "+"

        res = 0
        num = S[0]
        for j in range(n):
            if plus_lst[j] == 0:
                num += S[j + 1]

            if plus_lst[j] == 1:
                res += int(num)
                num = S[j + 1]

            if j == n - 1:
                res += int(num)

        ans += res

    print(ans)


if __name__ == "__main__":
    main()
