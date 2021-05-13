#!/usr/bin/env python3

def main():
    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))

    k = 0
    c = [[None for j in range(w)] for i in range(h)]
    p = 0
    for i in range(h):
        jlist = range(w) if i % 2 == 0 else reversed(range(w))
        for j in jlist:
            c[i][j] = p + 1
            a[p] -= 1
            if a[p] == 0:
                p += 1
            k += 1
        print(" ".join(str(x) for x in c[i]))

if __name__ == "__main__":
    main()
