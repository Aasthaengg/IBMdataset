import sys, math
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def main():
    N, K = map(int, input().split())

    """
    gcd(a1,...,aN) = dになる時を考える。もしこの個数がわかれば\sum_dして答えを得る。
    （決め打ち二分探索的な発想として出てくるのか？？？）
    これはa1,...,aNがすべてdの倍数のときと予想が立つが、すぐにgcd=2d, 3d,...の場合もありうると気づく。
    しかしこの考察から
            gcd(a1,...,aN)がdの倍数になる(a1,...,aN)の個数 = (K // d)^N
    という式を得る。

    同様にgcd(a1,...,aN)=(2dの倍数), gcd(a1,...,aN)=(3dの倍数)なる(a1,...aN)の個数もすぐ求まるので、
    kd <= Nなるなるべく大きなkを考えて（そうするとgcd(a1,...,aN)=mdなる(a1,...aN)の個数がばっちり求まる）、
    あとはkを小さくしていきながら適当な引き算を施すことで答えが求まる。
    """

    count = [0] * (K + 1) # count[i] = (gcd(a1,...,aN) = iとなる(a1,...,aN)の組の数)
    for d in range(1, K + 1):
        count[d] = pow(K // d, N, mod)
    for d in range(K // 2 + 1, 0, -1):
        for m in range(2, K // d + 1):
            count[d] -= count[m * d]
            count[d] %= mod
    #print(count)
    ans = 0
    for i in range(1, K + 1):
        ans += count[i] * i
        ans %= mod
    print(ans)

if __name__ == "__main__":
    main()
