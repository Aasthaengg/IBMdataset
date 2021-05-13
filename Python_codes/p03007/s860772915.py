import heapq
from collections import defaultdict
N = int(input())
nums  = list(map(int, input().split(" ")))
# 正の数、負の数の個数で操作をコントロール？
p_count = 0
m_count = 0
pos = []
minus = []
for num in nums:
    if num < 0:
        m_count += 1
        minus.append(num)
    else:
        p_count += 1
        pos.append(num)
pos.sort()
minus.sort() #小さい順番
途中式 = []
if N == 2:
    x = max(nums) 
    y = min(nums)
    print(max(nums) - min(nums))
    print(x, y)
else:
    #正の数を一つにして、そこから引きまくる
    if m_count == 0: #マイナスが無かったら作る
        x = min(pos)
        y = max(pos)
        途中式.append((x, y))
        minus.append(x - y)
        pos.remove(x)
        pos.remove(y)
        p_count -=2
        m_count += 1

    if p_count > 1: # 正が複数あったら、マイナスから引くことで減らしていく
        for i in range(p_count - 1):
            #マイナスから正が1個になるまで引いていく
            x = minus.pop()
            y = pos.pop()
            途中式.append((x,y))
            minus.append(x- y)
    elif p_count == 0 : #正が一つも無かったら、作る
        x = minus.pop()
        y = minus.pop()
        途中式.append((x, y))
        pos.append(x - y)

    x = pos.pop()
    for i in minus:
        y = i
        途中式.append((x, y))
        x -=y
    print(x)
    for temp in 途中式:
        x,y = temp
        print(x,y)