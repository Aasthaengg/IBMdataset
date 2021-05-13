



N,M,Q = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(M)]
PQ = [tuple(map(int, input().split())) for _ in range(Q)]


"""
pを含むpの右で出発して、qを含むqの左で停止する列車の本数を求める

愚直解だと、各クエリに対し各列車が当てはまるか見ていけばよい。が、計算量がO(M*Q)とかになるはずなので、到底間に合わない。
N,Mが10**5オーダーなので、各クエリに対し、O(1)とか、１でなくてももうちょっと少ないオーダーでで解答できると間に合う感じ。

各クエリに対し、毎回「列車１はここからここまでを走ってて～」を重複計算するのが無駄。
重複計算は前処理で解消するのが典型的な方法のはず。
区間に対して数え上げをする場合は累積和がよく使われる気がする。今回は二次元累積和。

"""

trains = [[0 for _ in range(N)] for _ in range(N)]
for l,r in LR:
    trains[l-1][r-1] += 1

# 累積和にする
for l in range(N):
    for r in range(l+1,N):
        trains[l][r] = trains[l][r-1] + trains[l][r]


for p,q in PQ:
    ans = 0
    for l in range(p-1, q):
        ans += trains[l][q-1]
    print(ans)