def main():
    S = input()
    n = len(S) - 1
    ans = 0

    for i in range(2 ** n):
        c = S[0]
        for j in range(n):
            if (i >> j) & 1 == 1:
                c += "+"
            c += S[j + 1]
        t = list(map(int, c.split("+")))
        ans += sum(t)

    print(ans)


if __name__ == "__main__":
    main()
