#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline
n, k = map(int, (input().split()))
print(n - k + 1)
