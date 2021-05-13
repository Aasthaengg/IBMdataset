import math
n, p = map(int, input().split())
s = input()

def nCr(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ans = 0
if p == 2 or p == 5:
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i + 1
else:
    # dp = [0] * p
    # dp[0] = 1
    # tmp = 0
    # for i in range(n)[::-1]:
    #     tmp = (int(s[i]) * pow(10, n - i - 1, p) + tmp) % p
    #     print(tmp)
    #     ans += dp[tmp]
    #     dp[tmp] += 1
    # print(dp)

    # ベースの考え方。https://drken1215.hatenablog.com/entry/2020/03/08/020200
    # 素数pで割ったあまりは、0, 1, 2, ... p - 1になる。
    # 例えば、s=152467, p=3とする
    # 0 mod 3 = 0 (単独でも1つになるので、便宜上加える)
    # 7 mod 3 = 1
    # 67 mod 3 = 1
    # 467 mod 3 = 2
    # 2467 mod 3 = 1
    # 52467 mod 3 = 0
    # 152467 mod 3 = 1
    # となる。
    # 例えば、x mod 3 = 1について、考える。これは、7, 67, 2467, 152467の4つある。
    # これから、67 - 7 = 60で、3で割り切れる。2467 - 7 = 2560で、3で割り切れる。
    # このように、4つのうち2つを組み合わせれば、あまりの数が同じなので、p(3)で割り切れる組み合わせ
    # を作ることができる。
    # 467 mod 3 = 2については、あまりが2はコレしかないので、組み合わせることはできず、0となる。
    # また、あまりが2のものと、あまりが1のもの2個で組み合わせることはできない。なぜなら、
    # 467-67-7で組み合わせたところで、67と7が互いに相殺してしまうし、結果も393という、sの中に存在しない文字になるからである。
    # 基本はこれであり、下記のようになるが、これでは遅い（調べたところ、(int(s[i:])) % pが）。
    # dp = [0] * p
    # dp[0] = 1
    # tmp = 0
    # for i in range(n)[::-1]:
    #     tmp = (int(s[i:])) % p
    #     dp[tmp] += 1
    # for i in dp:
    #     ans += nCr(i, 2)
    dp = [0] * p
    dp[0] = 1
    tmp = 0
    for i in range(n)[::-1]:
        tmp = (int(s[i]) * pow(10, n - i - 1, p) + tmp) % p
        dp[tmp] += 1
    for i in dp:
        ans += nCr(i, 2)
print(ans)