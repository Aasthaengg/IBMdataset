import sys
input = sys.stdin.readline

from heapq import heapify, heappop, heappush

N, D, A = map(int, input().split())
XH = []
XH_append = XH.append
for _ in range(N):
    x, h = map(int, input().split())
    XH_append((x, 0, h))

heapify(XH)
atk_cnt = 0
ans = 0
while XH:
    x, t, h = heappop(XH)
    if t == 0: #新しいのが出てきたタイミング
        if atk_cnt * A >= h:
            continue
        
        remain = h - atk_cnt * A #攻撃が足りない場合、追加する
        new_atk = (remain + A - 1) // A
        heappush(XH, (x + 2 * D, 1, new_atk))

        ans += new_atk
        atk_cnt += new_atk
    
    else:
        atk_cnt -= h

print (ans)
