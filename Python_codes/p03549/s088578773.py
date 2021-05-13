# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
ret = (1900 * m + 100 * (n-m)) * 2**m
print(ret)