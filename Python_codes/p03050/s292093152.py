
def resolve():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        divisors.sort()
        return divisors

    N = int(input())

    # N //m = k,  N%m = k  kは同じ値
    # N = k*m + k : 商と余りを計算したらNになる
    # N = k(m+1)より、m = (N//k)-1 -> m = 約数 - 1

    div = make_divisors(N)
    ans = 0
    for k in div[1:]:  # 1より大きい値からスタート
        m = k - 1
        if m <= 0:
            continue
        if N // m == N % m:
            ans += m

    print(ans)


if __name__ == "__main__":
    resolve()