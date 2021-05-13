def gcd(x, y):
    '''
    最大公約数の計算
    '''
    if y == 0:
        return x
    return gcd(y, x % y)
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# いずれか2つの数字のGCDが1 必ずTrue
# いずれか2つの数字のGCDが2 かつ Ai - K % 2 == 0 のものが存在する場合 True
# いずれか2つのGCDが計算できれば、答えが導けるが、いずれか2つの組み合わせはA * (A-1) // 2通りあるから間に合わない
# 累積GCDで1になる → どうにかこうにか1にできる
# 累積GCDで2になる → どの組み合わせをとっても2にしかならない


def main():
    ma = max(A)
    if ma < K:
        return False
    if K in A:
        return True
    g = A[0]
    for a in A:
        g = gcd(g, a)
    for a in A:
        if (a-K) % g == 0:
            return True
    return False


if main():
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

