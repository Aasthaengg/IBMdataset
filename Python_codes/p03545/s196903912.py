# ABC079 C問題 Train Tickets
"""
切符に４つの0以上9以下の整数A,B, C, Dが整理番号として順にかかれている。
Aop1Bop2Cop3D = 7　となるように、op1,2,3,に'+'または'-'を入れて式を作る。
答が存在しない入力は与えられず、また答が複数ある場合はどれを出力してもよい。
＜制約＞
0 <= A,B,C,D<=9
入力は整数
答が存在しない入力は与えられない
"""
n = list(int(x) for x in input())
op_cnt = len(n) - 1 #隙間の数

l = []
for i in range(1 << op_cnt):
    op = ['-'] * op_cnt
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - j -1] = '+'
            l.append(op)

for operators in l:
    expression = f"{n[0]}{operators[0]}{n[1]}{operators[1]}{n[2]}{operators[2]}{n[3]}"
    if eval(expression) == 7:
        print(f"{expression}=7")
        break




