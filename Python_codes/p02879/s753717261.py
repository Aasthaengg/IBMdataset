#!/usr/bin/env python3
A = [int(s) for s in input().split()]
print(A[0] * A[1] if sum(map(lambda x: 1 <= x <= 9, A)) == 2 else -1)
