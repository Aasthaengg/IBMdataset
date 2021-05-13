def main():
    s = sorted(input())
    print("Yes" if s[0] == s[1] and s[2] == s[3] and s[0] != s[3] else "No")


if __name__ == "__main__":
    main()
