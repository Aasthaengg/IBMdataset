if __name__ == "__main__":
    s = input()
    k = int(input())

    s_num = [0] * len(s)
    res = k
    for i in range(len(s)):
        tmp = ord(s[i]) - 97
        if tmp != 0 and 26 - tmp <= res:
            res -= (26 - tmp)
            s_num[i] = 0
        else:
            s_num[i] = tmp

    res %= 26

    s_num[-1] += res

    ans = ''
    for i in s_num:
        ans += chr(i + 97)

    print(ans)
