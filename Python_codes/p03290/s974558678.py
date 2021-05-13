# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# bit全探索
D, G = lr()
PC = [lr() for _ in range(D)]
answer = 10 ** 5
for pattern in range(1<<D):
    # patternが1のところはコンプリートボーナス
    temp = 0
    cnt = 0
    for i in range(D):
        if pattern>>i & 1:
            temp += PC[i][1] + (i+1) * 100 * PC[i][0]
            cnt += PC[i][0]
    j = D-1  # 残りは配点の多い問題から, 0-indexed
    while temp < G:
        if j < 0:
            break
        if pattern>>j & 1:
            j -= 1
            continue
        remain = G - temp
        point = (j + 1) * 100
        problems = (remain + point - 1) // point
        problems = min(problems, PC[j][0])
        cnt += problems
        temp += point * problems
        j -= 1
    else:
        if cnt < answer:
            answer = cnt

print(answer)
