#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Linear Search
n ????????´??°???????????°??? S ??¨???q ????????°????????´??°???????????°??? T ??????????????????
T ?????????????????´??°????????§ S ?????????????????????????????° C ???????????????????????°????????????????????????????????????
"""

def main():
    """ ????????? """
    n = int(input())
    S = list(input().split())
    q = int(input())
    T = list(input().split())

    cnt = {}
    for i in range(n):
        for j in range(q):
            if S[i] == T[j]:
                cnt[T[j]] = 1
                break
    print(len(cnt))


if __name__ == '__main__':
    main()