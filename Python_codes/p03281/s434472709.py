#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())

    ans = 0
    for i in range(1, N + 1, 2):
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c == 8:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
