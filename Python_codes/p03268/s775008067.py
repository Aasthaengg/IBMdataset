#!/usr/bin/env python3
n, k = map(int, input().split())
if k % 2:
    ans = (n // k) ** 3
    print(ans)
else:
    # 全て偶数、or 全て奇数
    ans = ((n + k // 2) // k) ** 3 + (n // k) ** 3
    print(ans)
