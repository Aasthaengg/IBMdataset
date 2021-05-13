# vim: fileencoding=utf-8


def main():
    d = {}
    n = int(input())
    for i in range(n):
        s = input()
        v = d.get(s, 0)
        d[s] = v + 1

    m = int(input())
    for i in range(m):
        s = input()
        v = d.get(s, 0)
        d[s] = v - 1
    ans = 0
    for i in d.values():
        if i > ans:
            ans = i
    print(ans)


if __name__ == "__main__":
    main()
