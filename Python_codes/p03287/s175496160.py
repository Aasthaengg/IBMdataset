#!/usr/bin/env python3

from collections import defaultdict

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for x in a:
        s.append((s[-1] + x) % m)
    cnt = defaultdict(int)
    for i, v in enumerate(s):
        cnt[v] += 1
    res = 0
    for k, v in cnt.items():
        res += v * (v - 1) // 2
    print(res)

if __name__ == "__main__":
    main()
