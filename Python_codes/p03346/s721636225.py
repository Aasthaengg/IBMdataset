N = int(input())
P = [int(input()) for _ in range(N)]


"""
t, t+1, t+2,... のように、差が１かつ単調増加で並んでいる部分列の最大長さが動かさないでいい数。
なので、２が１より右にあるか、３が２より右にあるか、...を、見ていき、t+1がtの右にない時点である部分列は終わり。
その最大長さを要素数から引いたものが答え

"""
idxs = [0] * (N+1)
for i in range(N):
    idxs[P[i]] = i # それぞれの数字の場所を記録

cnt = 1
max_len = 1
for i, j in zip(idxs[1:], idxs[2:]):
    if i < j:
        cnt += 1
        max_len = max(cnt, max_len)
    else:
        cnt = 1

print(N - max_len)
