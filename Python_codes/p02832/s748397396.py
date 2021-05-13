#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = 0
    n = 1
    for i in range(N):
        if a[i] != n:
            ans += 1
        else:
            n += 1
    if ans == N:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
