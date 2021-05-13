def main():
    S = input()

    for i in range(2 ** 3):
        c = S[0]
        for j in range(3):
            if (i >> j) & 1:
                c += "+"
            else:
                c += "-"
            c += S[j + 1]
        if eval(c) == 7:
            print(c + "=7")
            exit()


if __name__ == "__main__":
    main()
