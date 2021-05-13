# 今回はもし組み合わせがあるとしたらa1=0である組み合わせが確実にある。
# なぜなら、a1, a2, a3をxだけ引いた分b1, b2, b3をxだけ足せばつじつまがあうから
if __name__ == "__main__":
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    c = [c1, c2, c3]
    a = [0, 0, 0]
    b = [c1[0], c1[1], c1[2]]
    a[1] = c2[1] - b[1]
    a[2] = c3[1] - b[1]
    flg = True
    for i in range(3):
        for j in range(3):
            flg = flg&(a[i]+b[j] == c[i][j])
    if flg:
        print('Yes')
    else:
        print('No')