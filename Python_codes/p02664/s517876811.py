def main():
    s = list(input())

    for i in range(len(s)):
        if s[i] == "?":
            s[i] = "D"

    print(*s, sep="")


if __name__ == "__main__":
    main()
