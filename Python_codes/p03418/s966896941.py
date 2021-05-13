#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n, k = rli()
    if k == 0:
        print(n*n)
        return
    ans = 0
    for b in range(1, n+1):
        if b <= k:
            continue
        ans += (n // b)*(b-k)
        ans += max(0, n%b-k+1)
    print(ans)


if __name__ == '__main__':
    main()
