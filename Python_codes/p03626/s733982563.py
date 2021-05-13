def main():
    n = int(input())
    s1 = input()
    s2 = input()
    mod = 10**9 + 7
    h = "h"
    v = "v"
    d = ""
    i = 0
    while i < n:
        if s1[i] == s2[i]:
            d += v
        else:
            d += h
            i += 1
        i += 1
    c = 3 + 3 * (d[0] == h)
    for i in range(len(d) - 1):
        if d[i] == v:
            c = c * 2 % mod
        else:
            if d[i + 1] == h:
                c = c * 3 % mod
    print(c)

if __name__ == '__main__':
    main()