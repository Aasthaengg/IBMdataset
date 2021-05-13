#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    P = list(map(int, input().split()))

    ans = 1
    m = P[0]
    for i in range(1, N):
        if P[i - 1] < m:
            m = P[i - 1]
        if m >= P[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
