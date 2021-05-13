N=int(input())
A=list(map(int, input().split()))

l = 0
r = 0
s = 0 #対象区間のAND和
res = 0
#尺取り法
for l in range(N):
    while (r<N)and(s^A[r]==s+A[r]):
        #条件を満たす限りrightを右に進める
        s += A[r]
        r += 1
    #進めた幅だけ条件を満たす区間が存在したことになる
    res += r-l
    if l == r:
        #停滞した場合、rを1つ右にずらして次のlとrを等しくする
        r += 1
    else:
        # そうでない場合、lを一つ進めるので、今のlに対応する数を
        # AND和から引いておく
        s -= A[l]
print(res)