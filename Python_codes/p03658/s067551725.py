#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = [int(item) for item in input().split()]
l.sort(reverse=True)
ans = sum(l[:k])
print(ans)