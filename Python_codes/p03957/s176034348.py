def main():
    S = input()
    c = S.find("C")
    f = S[::-1].find("F")
    # print(c, len(S) - f - 1)
    if c >= 0 and f >= 0 and c < len(S) - f - 1:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
