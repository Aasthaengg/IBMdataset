def main():
    s = input()
    t = input()
    r = ""
    for l in range(len(s)):
        if s[l] != t[l]:
            r += s[l]
    if len(r) > 0:
        print("No")
        return
    else:
        print("Yes")
        return


main()