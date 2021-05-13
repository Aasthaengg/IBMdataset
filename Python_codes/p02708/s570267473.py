N, K = map(int, input().split())
MOD = 10 ** 9 + 7

# low, high それぞれ取りうる最小の値と最大の値
low, high = 0, 0
ans = 0
# x: 任意の数をx個取った時を想定してループを回すための変数
for x in range(1, N + 2):
    # lowは 0 + 1 +... K-1までの値を足すことになる(そうすればK個任意の数を選んだ時の最小値となる)
    # highは K + K+1 + ... + Nまでの値を足すことになる(そうすればK個任意の数を選んだ時の最大値となる)
    low += x - 1
    high += N - x + 1
    if x >= K:
        ans += (high - low + 1)
        ans %= MOD

print(ans)