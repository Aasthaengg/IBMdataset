def main():
    s = input()

    l = 0
    r = len(s) - 1

    ret = 0
    while l < r:
        lc, rc = s[l], s[r]

        if lc == rc:
            l += 1
            r -= 1
            continue

        if lc == 'x':
            ret += 1
            l += 1
            continue

        if rc == 'x':
            ret += 1
            r -= 1
            continue

        print(-1)
        return

    print(ret)


if __name__ == '__main__':
    main()
