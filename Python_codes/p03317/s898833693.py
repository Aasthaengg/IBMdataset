#!/usr/bin/env python3
n, k = map(float, input().split())
ans = -(-(n-1) // (k-1))
print(int(ans))