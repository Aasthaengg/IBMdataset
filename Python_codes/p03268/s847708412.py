n,k = map(int,input().split())

"""
Kが奇数なら, a=b=c=0(mod K)のみ
Kが偶数なら, a=b=c=K/2(mod K)「も」
"""

# n以下のmod Kがrの数の個数
def f(r):
    if r == 0: r = k
    return len(range(r, n + 1, k))

res = 0

# = 0
res += f(0) ** 3

# = k / 2
if k % 2 == 0:
    res += f(k // 2) ** 3

print(res)
