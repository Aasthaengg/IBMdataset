#! /usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A, B, C = map(int, input().split())
    if A == B and B == C:
        print('Yes')
    else:
        print('No')
