#!/usr/bin/env python3

A, B = map(str, input().split())

if A == B:
    print('=')
elif A < B:
    print('<')
else:
    print('>')
