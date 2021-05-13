#!/usr/bin/env python3
a, b, k = map(int, input().split())
if (b - a) // 2 + 1 < k:
    print(*range(a, b + 1), sep="\n")
else:
    print(*sorted(set([*range(a, a + k)] + [*range(b - k + 1, b + 1)])),
          sep="\n")
