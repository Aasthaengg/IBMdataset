# coding: utf-8

# https://atcoder.jp/contests/abc090/tasks/arc091_a
# 15:17-15:26 done


def main():
    n, m = map(int, input().split())

    if n == 1:
        if m == 1:
            return 1
        else:
            return m-2
    
    if m == 1:
        if n == 1:
            return 1
        else:
            return n-2
    
    return (n-2)*(m-2)


print(main())
