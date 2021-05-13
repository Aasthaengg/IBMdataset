#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, m, d = [int(i) for i in input().split()]

"""
from scipy.special import perm, comb

d == 0
def expectation_0(n, m, d):
    return sum([i * comb(m-1, k) * (n/n**2)**k * (1 - n/n**2)**(m-1-k) for k in range(0, m-1)])

d != 0
def expectation_0(n, m, d):
    return sum([i * comb(m-1, k) * (2(n-d)/n**2)**k * (1 - 2(n-d)/n**2)**(m-1-k) for k in range(0, m-1)])

def expectation(p, m):
        return sum([k * comb(m-1, k) * p**k * (1 - p)**(m-1-k) for k in range(0, m-1)])
"""
if d == 0:
    p = 1 / n  # n / n**2
    print((m - 1) * 1/n)

else:
    p = 2 * (n - d) / n**2
    print((m - 1) * p)
