#!/usr/bin/env python3

a, b, c = map(int, input().split())
A = sorted([abs(a-b), abs(a-c), abs(b-c)])

print(A[1]+A[0])
