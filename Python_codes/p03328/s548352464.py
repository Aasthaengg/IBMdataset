# coding: utf-8

# https://atcoder.jp/contests/abc099/tasks
# 15:00-


def main():
    a, b = map(int, input().split())
    dif = b - a
    
    return dif * (dif-1) // 2 - a


print(main())
