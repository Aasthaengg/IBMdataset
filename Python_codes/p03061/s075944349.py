#!/usr/bin/env python3

#import
import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

class SegTree:
    def __init__(self, segfunc, e, v, init_val = None):
        """
        segfunc: function 区間にしたい操作\n
        e: Any 単位元\n
        v: int or List 要素数か格納する配列\n
        init_val: Any 初期値
        """
        self.segfunc = segfunc
        self.e = e
        self.init_val = init_val if init_val != None else e
        if isinstance(v, int):
            v = [self.init_val] * v
        self.n = len(v)
        self.log = (self.n).bit_length()
        self.size = 1 << self.log
        self.tree = [e] * 2 * self.size
        # 1-indexedなのでtree[1:self.size]がN-1要素
        # tree[self.size:self.size + N]が配列
        for i in range(self.n):
            self.tree[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def set(self, k, x) -> None:
        """
        k番目の値をxに更新\n
        k: index(0-indexed)\n
        x: update value
        """
        k += self.size
        self.tree[k] = x
        for i in range(1, self.log + 1):
            self._update(k >> i)

    def get(self, k):
        """
        a[k]を返す\n
        k: index(0-indexed)
        """
        assert 0 <= k < self.size
        return self.tree[k + self.size]

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る\n
        l: index(0-indexed)\n
        r: index(0-indexed)
        """
        res = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

    def all_query(self):
        """
        全範囲にsegfuncしたものを得る
        """
        return self.tree[1]

    # 二分探索実装、いる？

    def _update(self, k):
        self.tree[k] = self.segfunc(self.tree[k * 2], self.tree[k * 2 + 1])

seg = SegTree(math.gcd, 0, A)

ans = 0

for i in range(N):
    ans = max(ans, math.gcd(seg.query(0, i), seg.query(i + 1, N)))

print(ans)
