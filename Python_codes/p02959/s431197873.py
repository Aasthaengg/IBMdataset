# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 合計で倒せる数
cnt = 0
# 次の街を助けることのできる数
help_cnt = 0
for i in range(n):
    # 自分の街で倒す数 = min(街のモンスター - 前の街の勇者が助けた数, 自分が倒せる数)
    now_kill_cnt = min(a[i]-help_cnt, b[i])

    # 次の街を助けることのできる数を更新
    # min(次の街のモンスター数, 余力)
    help_cnt = min(a[i+1], b[i]-now_kill_cnt)
    cnt += now_kill_cnt
    cnt += help_cnt


print(cnt)
