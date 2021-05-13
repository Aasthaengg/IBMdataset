c = [list(map(int, input().split())) for i in range(3)]

# a1,a2,a3を++、b1,b2,b3を--してもcは変わらない
# うまいことやればa1を0にできる、これを仮定する
# 第一行からbを求める
# 第一列からaを求める

b = [c[0][0], c[0][1], c[0][2]]
a = [0, c[1][0] - b[0], c[2][0] - b[0]]

# 仮のa,bが求まった、これが9マス全体で成り立つか調べる
for i in range(3):
    for j in range(3):
        if a[i] + b[j] != c[i][j]:
            print('No')
            exit()

print('Yes')
