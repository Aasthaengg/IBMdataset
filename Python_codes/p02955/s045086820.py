# E - Max GCD ★

def slvDivisor(summary):
    divisor = set()
    for d in range(1, int(summary ** 0.5) + 1):
        if summary % d == 0:
            divisor.add(d)
            divisor.add(summary // d)
    return divisor



input1 = list(map(int, input().split()))
n = input1[0]
k = input1[1]
a = list(map(int, input().split()))

# 和の約数を求める
sumA = sum(a)
divisor = slvDivisor(sumA)

# 各値を約数で割った際の余りも約数の整数倍（i倍とする）になるはず
# → ＋－する操作はその余りを他の値に移動して約数を作る操作になる
# → 余りが小さい値から大きい値へ余りを寄せていくのが効率的
# → 寄せきると約数 * i個、0 * (N - i)個の2ブロックに分かれる
# → 寄せきるまでの回数がk以下ならOK
for d in sorted(divisor, reverse=True):
    modA = [x % d for x in a]
    modA.sort()
    i = sum(modA) // d
    cnt = sum(modA[:-i])
    if cnt <= k:
        print(d)
        break