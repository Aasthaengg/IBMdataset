def main():
    n = int(input())
    s = input()
    x = 0
    ans = 0

    for ch in s:
        if ch == "I":
            x += 1
        else:
            x -= 1
        ans = max(ans, x)

    print(ans)


if __name__ == "__main__":
    main()
