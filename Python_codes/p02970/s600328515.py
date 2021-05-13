#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc134/tasks/abc134_a

n, d = map(int, input().strip().split())

persons = (n - 1) // (2 * d + 1) + 1

print(persons)
