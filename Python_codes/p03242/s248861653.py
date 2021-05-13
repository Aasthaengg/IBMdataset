def main():
    n = input()
    ans = ""

    for ch in n:
        if ch == "1":
            ans += "9"
        elif ch == "9":
            ans += "1"

    print(ans)


if __name__ == "__main__":
    main()
