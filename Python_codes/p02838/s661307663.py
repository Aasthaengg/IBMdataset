n = int(input())
a = list(map(int, input().split()))

mod = 10**9 + 7
ans = 0
# 制約より、aはそれぞれ60桁以内で表せる
# i+1(=1,2,...,60)桁目についてそれぞれ考える
for i in range(60):
    k = 1 << i  # k = 100....00(2) = 2**i(10)
    cnt_1 = 0
    cnt_0 = 0

    for ai in a:
        if k & ai:
            cnt_1 += 1
        else:
            cnt_0 += 1
    # 1 XOR 0 = 1 となる個数 = cnt_1 * cnt_0
    # 桁が違うのでk(== 2**0, 2**1, 2**2,...)をかける必要がある
    ans += ((k % mod) * cnt_1 * cnt_0) % mod

print(ans % mod)
