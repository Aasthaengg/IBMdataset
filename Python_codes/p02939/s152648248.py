def main():
    s = input()
    ans = 0
    pre = ""
    is_same = False

    for i in range(len(s)):
        if is_same:
            pre += s[i]
            ans += 1
            is_same = False
            continue

        if pre != s[i]:
            ans += 1
            pre = s[i]
        else:
            is_same = True

    print(ans)


if __name__ == "__main__":
    main()
