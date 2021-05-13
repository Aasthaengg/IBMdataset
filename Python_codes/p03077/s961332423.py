#!/usr/bin/env python3
n, *s = map(int, open(0).read().split())
print(-(-n // min(s)) + 4)
