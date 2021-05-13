N, M = map(int, input().split())
inf = int(1e10)
dp = [inf] * (1 << N) #1をNだけシフトする 2**B

#鍵をビットで表す　dp[i]は鍵の状態iにできる最小費用を
dp[0] = 0
bits = set()
bits.add(0)

for i in range(M):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    # cを状態keyに変換
    key = 0
    for t in c:
        key += 1 << (t - 1)
    # bits内のbitとkeyのORを更新
    # 更新したbitはbitsに追加
    add_bits = set()
    for bit in bits:
        tmp = bit | key
        if dp[bit] + a < dp[tmp]:
            dp[tmp] = dp[bit] + a
            add_bits.add(tmp)
    bits |= add_bits
    
if dp[(1 << N) - 1] == inf:
    print(-1)
else:
    print(dp[(1 << N) - 1])