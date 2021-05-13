#合計宿泊数
N = input()
#通常宿泊数
K = input()
#通常宿泊費
X = input()
#割引宿泊費
Y = input()
#宿泊日数カウント
S = 1
#合計金額カウント
P = 0

#合計日数が割引日数以上
if int(N) >= int(K):
    #通常宿泊出力
    while S <= int(K):
        P = P + int(X)
        S = S + 1

    #割引宿泊出力
    while S <= int(N):
        P = P + int(Y)
        S = S + 1
#合計日数が割引日数未満
else :
    #通常宿泊出力
    while S <= int(N):
        P = P + int(X)
        S = S + 1

#合計金額出力
print(P)