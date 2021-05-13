def main():
    n = int(input())
    s = input()
    white = s.count(".")
    ans, black = white, 0
    for i in range(n):
        if s[i] == ".":
            white -= 1
        else:
            black += 1
        tmp = black + white
        if tmp < ans:
            ans = tmp
    print(ans)


if __name__ == "__main__":
    main()
