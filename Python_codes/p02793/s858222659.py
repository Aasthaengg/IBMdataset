#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = lcm(a)
    b = [c // ai for ai in a]
    print(sum(b) % (10 ** 9 + 7))

def lcm(li):
    res = 1
    for x in li:
        res *= (x // gcd(res, x))
    return res

def gcd(x, y):
    if x < y:
        x, y = y, x  # x >= y
    while y > 0:
        r = x % y
        x = y
        y = r
    return x
if __name__ == "__main__":
    main()
