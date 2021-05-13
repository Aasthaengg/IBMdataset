def slove():
    import sys
    input = sys.stdin.readline
    s = str(input().rstrip('\n'))
    ss = ""
    for i in range(len(s)):
        if ss == "" and s[i] == "C":
            ss = s[i]
        elif ss == "C" and s[i] == "F":
            print("Yes")
            exit()
    print("No")


if __name__ == '__main__':
    slove()
