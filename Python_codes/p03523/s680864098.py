def mach_akiba(s, i):
    if len(s) == 9 or i > len(s):
        if s == "AKIHABARA":
            return True
        return False

    return mach_akiba(s, i+1) or mach_akiba(s[:i]+"A"+s[i:], i+1)


def main():
    s = input()

    if len(s) > 9:
        print("NO")
    elif mach_akiba(s, 0):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
