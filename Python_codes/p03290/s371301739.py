# coding: utf-8

import math
import re
import numpy as np
import copy

S = input().split(" ")
D = int(S[0])
G = int(S[1])

p_n = []
c_n = []

for i in range(D):
    line = input().split(" ")
    p = int(line[0])
    c = int(line[1])
    p_n.append(p)
    c_n.append(c)

#十分大きい数で初期化
ans = 1000000

#ボーナス取得の有無を分配する関数（2^D通り）
def CombiBonus(flag):
    #最後まで到達した場合
    if len(flag) == D:
        #最小値の計算関数へ
        CalcMin(flag)

    else:
        #次のボーナスを取得するか否か
        non_use = flag + "0"
        use = flag + "1"
        CombiBonus(non_use)
        CombiBonus(use)

#最小回数を計算する関数
def CalcMin(flag):
    global ans

    #print(flag)

    #未回答問題数を格納するリスト
    unsolved = copy.copy(p_n)
    #現在のスコア
    score = 0
    #現在解いた問題数
    cnt = 0

    #ボーナス獲得している場合、全て解いているので反映
    for i in range(D):
        if flag[i] == "1":
            unsolved[i] = 0
            score += (i+1)*p_n[i]*100
            score += c_n[i]
            cnt += p_n[i]

    #これから解く問題の難易度
    current_d = D-1
    #スコアがG以上になるまで、難しい問題から優先して解き続ける
    while score < G:
        #2問以上残っている場合、同じ難易度のものを解く
        if unsolved[current_d] > 1:
            unsolved[current_d] -= 1
            score += (current_d+1)*100
            cnt += 1

        #そうでない場合、次の難易度へ
        else:
            current_d -= 1
            #0を下回る場合、終了
            if current_d < 0:
                return

    #print(cnt, score)

    #問題数が最小値かを判定
    if cnt < ans:
        ans = cnt

#探索
flag = ""
CombiBonus(flag)

print(ans)

