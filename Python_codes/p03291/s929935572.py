def main():
    """
    1 <= i < j < k <= |T|
    Ti = A
    Tj = B
    Tk = C
    """
    S = input()
    ans3 = cumsum(S)
    print(ans3)


def cumsum(S):
    """
    考えたときに累積和が浮かんだ
    ABCとあるので
    i文字目までのA相当の数、つまり?も含んだ数
    これをBとCにも適用する
    Aを決め打ちで進めるとBも走査することになる
    Cは定数倍で求められるが、|S|^2: TLE で意味がない

    ここで断念していろいろ調べると
    Bを決め打ちすれば
    A: 0-(B-1)
    C: (B+1)-N
    なのでNでおｋ

    と、思ったがWAと同じ間違いをしている
    3^q パターンをきちんと考える
    """
    n = len(S)
    aa = [0 for _ in range(n+1)]
    cc = [0 for _ in range(n+1)]
    q = [0 for _ in range(n+1)]
    for i in range(n):
        aa[i+1] += aa[i] + int(S[i] == "A")
        cc[i+1] += cc[i] + int(S[i] == "C")
        q[i+1] += q[i] + int(S[i] == "?")

    ans = 0
    MOD = 10 ** 9 + 7
    for i in range(1, n-1):
        a = aa[i]
        c = cc[n] - cc[i+1]
        l = q[i]
        r = q[n] - q[i+1]
        # ABC の作り方
        # AB?: ? 1つをCに割り当てる
        # ?BC: ? 1つをAに割り当てる
        # ?B?: ? 2つをACに割り当てる
        if S[i] in ("B", "?"):
            ac = a * c * pow(3, l + r, MOD)
            aq, qc, qq = (0, 0, 0)
            if l + r - 1 >= 0:
                p = pow(3, l + r - 1, MOD)
                aq = a * r * p
                qc = l * c * p
            if l + r - 2 >= 0:
                qq = l * r * pow(3, l + r - 2, MOD)
            # print(a, c, l, r, ((l+r, l+r-1, l+r-2)), (ac, aq, qc, qq))
            # 3^x: xが負になるときに少数になってしまうので、float -> int にする必要がある
            # 上記が重いのでTLE: pow+mod引数で対応
            ans += ac + aq + qc + qq
            ans %= MOD

    return ans


if __name__ == '__main__':
    main()
