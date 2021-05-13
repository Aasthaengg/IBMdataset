def main():
    n = int(input())
    s = input()
    Q = int(input())
    t = [input().split() for _ in range(Q)]

    d = [0] * n + [1 << ord(c) - 97 for c in s]
    for i in range(n - 1, 0, -1):
        d[i] = d[i + i] | d[i - ~i]
    for q, a, b in t:
        i, s = int(a) + n - 1, 0
        if q < "2":
            d[i] = 1 << ord(b) - 97
            while i > 1:
                i //= 2
                d[i] = d[i + i] | d[i - ~i]
        else:
            j = int(b) + n
            while i < j:
                if i & 1:
                    s |= d[i]
                    i += 1
                if j & 1:
                    j -= 1
                    s |= d[j]
                i //= 2
                j //= 2
            print(bin(s).count("1"))


main()
