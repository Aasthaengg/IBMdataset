def main():
    s, t = input(), input()

    for _ in range(len(s)):
        if s == t:
            print("Yes")
            break
        s = s[-1] + s[:-1]
    else:
        print("No")


if __name__ == "__main__":
    main()
