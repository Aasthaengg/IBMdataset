def main():
    N, K = map(int, input().split())
    *V, = map(int, input().split())

    m = min(N, K)

    ans = 0
    for left in range(m + 1):
        _r = m - left
        for right in range(_r + 1):
            rest = K - left - right
            take = V[:left] + V[N - right:]
            take.sort()
            s = 0
            for x in take:
                if rest and x < 0:
                    rest -= 1
                    continue
                s += x
            ans = max(ans, s)
    print(ans)


if __name__ == '__main__':
    main()

# 操作回数はK回以内
# x=min(K,N)個取り出す
# K-x個戻せる
