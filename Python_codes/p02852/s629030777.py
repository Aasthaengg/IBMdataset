N,M = map(int,input().split())
S = input()
RS = S[::-1]

"""
ゴール側から考えれば、自然と辞書順最小になる。（気がする）
前処理で各セーフマスから最も近い前方のセーフマスの位置を求めておく。
nxSafe[i] =>　ゴールからスタートに進むとして、ゴールからiマス目の次のセーフゾーンのインデックス
"""
nxSafe = [None]*(N+1)
safe = N
for i in range(N-1,-1,-1):
    if RS[i] == "0":
        nxSafe[i] = safe
        safe = i

cur = 0
ans = []
while cur < N:
    tmp = cur
    while True:
        if tmp == N:
            break
        if nxSafe[tmp] - cur <= M:
            tmp = nxSafe[tmp]
        else:
            break
    if cur == tmp:
        print(-1)
        exit()
    ans.append(str(tmp-cur))
    cur = tmp
ans = ans[::-1]
print(" ".join(ans))