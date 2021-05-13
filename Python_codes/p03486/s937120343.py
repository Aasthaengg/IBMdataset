# vim: fileencoding=utf-8


def main():
    s = list(input())
    t = list(input())
    s.sort()
    t.sort(reverse=True)
    l = len(s)
    tl = len(t)
    if l > tl:
        l = tl
    for i in range(l):
        if s[i] == t[i]:
            continue
        if t[i] > s[i]:
            print("Yes")
            return
        print("No")
        return
    if l == tl:
        print("No")
        return
    print("Yes")


if __name__ == "__main__":
    main()
