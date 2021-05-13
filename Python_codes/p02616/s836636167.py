import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,K = LI()
    A = LI()

    ans = 1
    ma = max(A)
    if ma <= 0 and K % 2:
        # 最大値が0以下でKが奇数の場合
        x = sorted(A,reverse=True)
        # 大きいほうからK個の積
        for i in range(K):
            ans = (ans * x[i]) % MOD
        print(ans)
        return

    # 絶対値でソート
    x = sorted(A, key=lambda x: abs(x), reverse=True)
    m = 0
    # 絶対値が大きいほうからK個の積
    for i in range(K):
        ans = (ans * x[i]) % MOD
        if x[i] < 0: m += 1

    # K==Nか、マイナスが偶数、答えが0ならそのままリターン
    if K == N or m % 2 == 0 or ans == 0:
        print(ans)
        return
    # K+1個目が0なら、0でリターン
    if x[K] == 0:
        print(0)
        return

    # K個目まですべてマイナスなら
    if m == K:
        # K番目とK+1以降の最大値とを入れ替え
        ans = (ans * pow(x[K-1],MOD-2,MOD) * max(x[K:])) % MOD

    else:
        K1 = -1
        # K+1番目と符号が反対で絶対値が最大の数をK+2番目以降で探す
        for i in range(K+1,N):
            if x[K] * x[i] < 0:
                K1 = i
                break

        f0 = 0.0
        f1 = 0.0
        i0 = -1
        i1 = -1
        # K番目以内でK+1番目と符号が反対で最小の数を探す
        for i in range(K-1,-1,-1):
            if x[i] * x[K] < 0:
                i0 = i
                # 入れ替えた時の減少率
                f0 = x[K] / x[i]
                break

        if K1 >= 0:
            # K1が存在するとき、K番目以内でK1番目と符号が反対で最小の数を探す
            for i in range(K-1,-1,-1):
                if x[i] * x[K1] < 0:
                    i1 = i
                    f1 = x[K1] / x[i]
                    break

        if abs(f0) >= abs(f1):
            ans = (ans * pow(x[i0],MOD-2,MOD) * x[K]) % MOD
        else:
            ans = (ans * pow(x[i1],MOD-2,MOD) * x[K1]) % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()