def main():
    s = input()
    flag = True

    for i in range(len(s)):
        if i % 2 == 0:  # 奇数文字目
            if s[i] not in ["R", "U", "D"]:
                flag = False
                break
        else:  # 偶数文字目
            if s[i] not in ["L", "U", "D"]:
                flag = False
                break

    if flag:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
