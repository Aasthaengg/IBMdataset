#!/usr/bin/env python3

from functools import reduce

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    N = II()
    A = LII()
  
    mn = 10 ** 9
    n = 0
    ans = 0
    for a in A:
        ans += abs(a)
        mn = min(mn, abs(a))
        if a < 0:
            n += 1

    if n % 2 == 0:
        print(ans)
    else:
        print(ans - 2 * mn)

if __name__ == '__main__':
    main()
