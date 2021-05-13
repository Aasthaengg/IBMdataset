def slove():
    import sys
    input = sys.stdin.readline
    ie = False
    s = str(input().rstrip('\n'))
    for i in range(len(s)):
        if s[i] == "C":
            ie = True
        elif ie and s[i] == "F":
            print("Yes")
            exit()
    print("No")


if __name__ == '__main__':
    slove()
