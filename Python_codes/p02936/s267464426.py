# 初期入力 readlineだけで1950ms⇒1234ms
#                           PyPy   ⇒867ms
from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline
N,Q = (int(x) for x in input().split())

connection ={i:set() for i in range(1,N+1)}
for i in range(1,N):
    a,b = (int(i) for i in input().split())
    connection[a].add(b)
    connection[b].add(a)
nord_point = defaultdict(lambda: 0)
for i in range(1,Q+1):
    a,b = (int(i) for i in input().split())
    nord_point[a] +=b

#BSF

dq =deque()
start =1
dq.append(start)
passed =set()
counter_dic ={i:0 for i in range(1,N+1)}
counter_dic[start] =nord_point[start]
while len(dq) >0:
    now =dq.popleft()
    passed.add(now)
    for next in connection[now]:
        if next not in passed:
            #頂点のカウンター＝親のカウンター ＋ 頂点のポイント
            counter_dic[next] =counter_dic[now] +nord_point[next]
            dq.append(next)
#出力
print(*counter_dic.values())