# -*- coding: utf-8 -*-


def linear_search(S, T):
    count = 0
    for i in xrange(len(T)):
        if T[i] in S:
            count += 1
    return count

if __name__ == '__main__':
    n = input()
    S = map(int, raw_input().split())
    q = input()
    T = map(int, raw_input().split())

    print linear_search(S, T)