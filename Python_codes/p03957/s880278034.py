import collections


def main():
    s = list(input())
    if s.count("C") == 0 or s.count("F") == 0:
        print("No")
        return

    clen, flen = 0, 0
    for i in range(len(s)):
        if clen == 0:
            if s[i] == "C":
                clen = i
        if s[i] == "F":
            flen = i
    print("Yes" if flen > clen else "No")


if __name__ == '__main__':
    main()
