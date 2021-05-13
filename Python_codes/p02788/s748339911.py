import sys
input = sys.stdin.readline
import collections
from collections import deque
n,d,a= map(int, input().split())
x= [list(map(int, input().split())) for i in range(n)]

x.sort()
for i in range(n):
    x[i][1]=-(-x[i][1]//a)

# どのモンスターまで倒したか管理しながら進める。
# 累積ダメージを管理
qq=deque([])
ans=0
atk=0
for i in range(n):
    w=x[i][1]
    # ダメージの有効期限を超過している場合
    while len(qq)>0 and x[i][0] > qq[0][0]:
        atk-=qq[0][1]
        qq.popleft()

    if w-atk>0:
        ans+=w-atk
        # 有効期限　ダメージ
        qq.append([x[i][0]+2*d,w-atk])
        atk += w - atk
print(ans)
