# 約数のリストを得る
def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

N, M = map(int, input().split())
l = make_divisors(M)
# mの約数
res = 1
# 全ての約数において、kと仮定する
for k in l:
    x = M // k
    # この際、Mをkで除した数列bがN以上であるかを判定する
    if x >= N:
        res = max(res, k)
print(res)