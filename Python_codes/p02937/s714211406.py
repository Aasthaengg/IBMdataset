#!/usr/bin/env python3

from bisect import bisect_right

def main():
    s = input()
    t = input()
    indices = [[] for i in range(26)]
    n = len(s)
    for i in range(n):
        c = s[i]
        ic = ord(c) - ord("a")
        indices[ic].append(i)
    for i in range(26):
        if not indices[i]:
            continue
        indices[i].append(indices[i][0] + n)

    ptr = -1
    for c in t:
        ic = ord(c) - ord("a")
        if len(indices[ic]) == 0:
            print(-1)
            return
        nptr = bisect_right(indices[ic], ptr % n)
        ptr += indices[ic][nptr] - (ptr % n)

    print(ptr + 1)

if __name__ == "__main__":
    main()
