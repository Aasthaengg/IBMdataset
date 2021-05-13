def main():
    N = int(input())
    S = input()
    if len(set(S)) == 1:
        return print(0)
    w = S.count(".")
    b = 0
    ans = w
    for s in S:
        if s == "#":
            b += 1
        else:
            w -= 1
        ans = min(ans, b+w)
    print(ans)


if __name__ == '__main__':
    main()
