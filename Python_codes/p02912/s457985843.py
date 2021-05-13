# 優先度付きキューとか言うものが使えるかどうかが鍵になる
# pythonでは標準でheapqが使える．要するにヒープのこと．ただしヒープでは最小値しか取り出せないのでそこに注意する必要がある.
# 計算量はO(log(N))になる
N,M = map(int,input().split())
A = list(map(int,input().split()))
# 解法 bisectとsort(最初だけ)を使う
# dequeでbisectって使えんのかなぁ？
#A.sort()
#from collections import deque
#A = deque(A)
A = [-a for a in A]
import heapq
heapq.heapify(A)
import bisect
for i in range(M):
    a = heapq.heappop(A)
    new = a/2
    # listに挿入する．ただしpythonのlistは可変長配列なので，linked-listではない.それゆえ末尾や先頭以外への要素の挿入はO(N)かかる
    #bisect.insort_left(A,new)   # やってることはA.sort(bisect.bisect_left(A,new),new)．
    heapq.heappush(A,new)
import numpy as np
A = np.array(A,dtype=np.int64)
print(-A.sum())

