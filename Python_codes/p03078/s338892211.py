#!/usr/bin/env python3

import heapq

def main():
    x, y, z, k = map(int, input().split())
    a = list(reversed(sorted(map(int, input().split()))))
    b = list(reversed(sorted(map(int, input().split()))))
    c = list(reversed(sorted(map(int, input().split()))))
    q = [(-a[0] - b[0] - c[0], 0, 0, 0)]
    queued = {(0, 0, 0)}
    for i in range(k):
        v, s, t, u = heapq.heappop(q)
        print(-v)
        for e, f, g in [(s, t, u + 1), (s, t + 1, u), (s + 1, t, u)]:
            if e >= x or f >= y or g >= z:
                continue
            if (e, f, g) in queued:
                continue
            heapq.heappush(q, (-(a[e] + b[f] + c[g]), e, f, g))
            queued.add((e, f, g))

if __name__ == "__main__":
    main()
