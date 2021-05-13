# 解説AC
# 素直に立式してから因数分解
# そこから愚直に計算せず線形時間でできるように考える
MOD = 10**9 + 7


def main():
    N, M = (int(i) for i in input().split())
    X = [int(i) for i in input().split()]
    Y = [int(i) for i in input().split()]
    xl = 0
    yl = 0
    for i, x in enumerate(X):
        xl += i*x - (N-i-1)*x
    for i, y in enumerate(Y):
        yl += i*y - (M-i-1)*y
    ans = xl*yl
    ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
