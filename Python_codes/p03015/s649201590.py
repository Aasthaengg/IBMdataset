MOD = 10**9+7

L=input()
N = len(L)
ans = 0
num = 0 # Lの先頭iケタにおける1の個数
cum_one_cnt = [0]*(N+1)
for i in range(N):
    length = N-i-1
    if L[i] == "1":
        ans += pow(3, length, MOD) * pow(2, num, MOD) % MOD
        ans %= MOD
        num += 1 # 1を発見したので1つ加算

# 最後のパターンのみ特殊(フリーなケタがない)
ans += pow(2, num, MOD)
print(ans%MOD)