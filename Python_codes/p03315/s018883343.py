def main():
    s = input()
    ans = 0

    for ch in s:
        if ch == "+":
            ans += 1
        else:
            ans -= 1

    print(ans)


if __name__ == "__main__":
    main()
