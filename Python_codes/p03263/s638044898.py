#!/usr/bin/env python3

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        l = list(map(int, input().split()))
        a.append(l)

    hold = False
    opers = []
    for i in range(h):
        jlist = range(w) if i % 2 == 0 else reversed(range(w))
        for j in jlist:
            if not (i == j == 0):
                if hold:
                    opers.append((ipre + 1, jpre + 1, i + 1, j + 1))
            hold = (hold != (a[i][j] % 2 == 1))
            ipre = i
            jpre = j
    print(len(opers))
    for o in opers:
        p, q, r, s = o
        print(p, q, r, s)

if __name__ == "__main__":
    main()
