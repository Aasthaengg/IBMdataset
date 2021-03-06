# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:42:18 2020

@author: liang
"""
"""
【優先度付きキュー】
・ヒープ構造の部分順序付き木
・挿入、削除、最大値（最小値）の取り出し、要素の値の変更
　⇒　O(log n)
・ヒープ生成
　⇒O(n)
 【使い方】
  import heapq
  ●heapq.heapify(list) #最小値
  ●heapq.heapify(list(map(lambda x:int(x)*(-1),list))) #最大値は値をひっくり返す
  ●heapq.heappop(a)
  ●heapq.heappush(a,1)
"""

import heapq
N, M = map(int, input().split())
# -1倍する
A = [int(x)*(-1) for x in input().split()]
heapq.heapify(A)

#O(M) * O(log N)
for i in range(M):
    Max = heapq.heappop(A) * (-1)
    Max //= 2
    heapq.heappush(A, Max*(-1))
print(-sum(A))