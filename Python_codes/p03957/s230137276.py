def main():
    s = input().rstrip()
    a, b = len(s), -1
    for i in range(len(s)):
        if s[i] == "C":
            a = i
            break
    for i in reversed(range(len(s))):
        if s[i] == "F":
            b = i
            break
    if a < b:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
