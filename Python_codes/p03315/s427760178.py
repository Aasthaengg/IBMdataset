# coding: utf-8

# https://atcoder.jp/contests/abc101


def main():
    S = input()
    ans = 0
    for s in S:
        if s == "+":
            ans += 1
        else:
            ans -= 1
    
    return ans


print(main())
