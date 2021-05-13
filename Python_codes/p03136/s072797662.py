# -*- coding: utf-8 -*-

import sys

def main():
    input = sys.stdin.readline
    n = input()
    l = list(map(int, input().split()))
    max_l = max(l)
    l.remove(max_l)
    sum_l = sum(l)
    if max_l < sum_l:
        print("Yes")
    else:
        print("No")
    return


if __name__ == '__main__':
    main()