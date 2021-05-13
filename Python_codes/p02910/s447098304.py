def main():
    s = input()
    ans = True
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == "L":
            ans = False
        elif i % 2 == 1 and s[i] == "R":
            ans = False
    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()
