#!/usr/bin/env python3

def main():
    N, *a = map(int, open(0).read().split())

    a.sort(reverse = True)
    s = 0
    for i in range(N):
        s = s + a[2*i + 1]
    print(s)


main()