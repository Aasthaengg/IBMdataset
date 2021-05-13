def main():
    s = input()
    n = len(s)

    for i in range(n):
        for j in range(n - i + 1):
            if s[:i] + s[i + j:] == "keyence":
                print("YES")
                exit()
    else:
        print("NO")


if __name__ == "__main__":
    main()
