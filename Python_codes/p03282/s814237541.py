def main():
    s = input()
    k = int(input())
    index = k + 1

    for i in range(len(s)):
        if s[i] != "1":
            index = i
            break

    if index < k:
        print(s[index])
    else:
        print(1)


if __name__ == "__main__":
    main()
