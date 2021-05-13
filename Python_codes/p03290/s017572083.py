d,g = map(int, input().split())

pc = [list(map(int, input().split())) for _ in range(d)]

ans=float('inf')
for bit in range(2**d):
    b = 0
    score = 0
    num = 0
    # ボーナスを貰えるまで問題を解く場合を計算
    # bit探索し、ボーナスを貰うパターンを網羅する
    for i in range(d):
        if (bit >> i) & 1:
            # 問題を解いた点 + ボーナス
            score += pc[i][0] * (i+1) * 100 + pc[i][1]
            # 解いた問題数
            num += pc[i][0]
        else:
            # ボーナスを貰えるまで解かない問題の場合
            # この値には最終的にはボーナスを貰えるまでは解かない、最大点がもらえる問題の番号が入る
            b = i

    # ボーナスを貰えるまでは解かない問題による加点と回答の更新を行う
    for j in range(pc[b][0]):
        if score>=g and num<ans:
            ans=num
        score+=(b+1)*100
        num+=1

print(ans)