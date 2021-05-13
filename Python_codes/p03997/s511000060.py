#!/use/bin/env python3

from collections import defaultdict

(a, b, h) = [int(input()) for _ in range(0, 3)]

print((a + b) * h // 2)
