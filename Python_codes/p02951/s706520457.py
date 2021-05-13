#!/usr/bin/env python3
A,B,C = [int(s) for s in input().split()]

print(0) if B+C <= A else print(C-(A-B))
