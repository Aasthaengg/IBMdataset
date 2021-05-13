import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    s = input()
    k = int(input())

    lens = len(s)
    if len(s) == 1:
        print(k // 2)
        sys.exit()

    if k == 1:
        r2 = 0
        rt = 1
        c = ""
        flag = False
        for se in s:
            if c == se:
                flag = True
                rt += 1
            else:
                c = se
                if flag:
                    r2 += rt // 2
                    rt = 1
                    flag = False
        r2 += rt // 2
        print(r2)
        sys.exit()

    s_daburi = 0
    s_last = s[-1]
    while s_daburi < lens:
        if s[s_daburi] == s_last:
            s_daburi += 1
        else:
            break
    s1 = s + s_last * s_daburi

    r2 = 0
    rt = 1
    c = ""
    flag = False
    for se in s1:
        if c == se:
            flag = True
            rt += 1
        else:
            c = se
            if flag:
                r2 += rt // 2
                rt = 1
                flag = False
    r2 += rt // 2

    if s_daburi == lens:
        if k % 2 == 0:
            r = r2 * (k // 2)
            print(r)
            sys.exit()
        else:
            r = r2 * (k // 2) + lens//2
            print(r)
            sys.exit()

    r = r2
    s2 = s[s_daburi:] + s_last * s_daburi
    r2 = 0
    rt = 1
    c = ""
    flag = False
    for se in s2:
        if c == se:
            flag = True
            rt += 1
        else:
            c = se
            if flag:
                r2 += rt // 2
                rt = 1
                flag = False
    r2 += rt // 2

    s3 = s[s_daburi:]
    r3 = 0
    rt = 1
    c = ""
    flag = False
    for se in s3:
        if c == se:
            flag = True
            rt += 1
        else:
            c = se
            if flag:
                r3 += rt // 2
                rt = 1
                flag = False
    r3 += rt // 2
    if k == 2:
        print(r + r3)
    else:
        print(r + r3 + r2 * (k-2))



if __name__ == '__main__':
    main()
