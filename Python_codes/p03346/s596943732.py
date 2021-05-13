"""
連続する数は動かさず、それ以外を左右に分配していく
⇨並べ替えた後、昇順に連続しているかは、インデックスが昇順になっているかを見る
"""
import sys
input = sys.stdin.readline

n = int(input())
ps = {int(input()):i for i in range(n)}
cnt = 1
prev = 10**10
ans = 0
# 番兵
ps[n+1] = -1
for i in range(1,n+2):
    ind = ps[i]
    if prev < ind:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
    prev = ind
print(n-ans)