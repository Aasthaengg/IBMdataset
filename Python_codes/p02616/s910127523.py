def abc173_e():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    mod = 10**9 + 7

    A.sort(reverse=True)  # 符号付きの大きい順
    B = sorted(A, key=lambda x: abs(x), reverse=True)  # 絶対値の大きい順
    C = []

    if k == n:
        C = A  # 全部使う
    elif k % 2 == 1 and A[0] < 0:
        C = A[:k]  # 絶対値小さい順にk個
    else:
        plus = []
        minus = []
        for b in B[:k]:
            if b >= 0: plus.append(b)
            else: minus.append(b)

        if len(minus) % 2 == 1:
            # 積が負になるので入れ替え検討
            rem1, add1, rem2, add2 = None, None, None, None

            rem1 = minus[-1]  # 負値の絶対値最小
            add1 = max(B[k:])  # 残りものの正値の絶対値最大
            valid1 = (add1 >= 0)

            valid2 = False
            if plus:
                rem2 = plus[-1]
                add2 = min(B[k:])  # 負値の絶対値最大
                valid2 = (add2 < 0)

            if valid1 and valid2:
                if add1 * rem2 > rem1 * add2:
                    minus[-1] = add1
                else:
                    plus[-1] = add2
            elif valid1:
                minus[-1] = add1
            elif valid2:
                plus[-1] = add2

        C = plus + minus

    ans = 1
    for c in C:
        ans *= c
        if ans < 0: ans += mod
        ans %= mod
    print(ans)

if __name__ == '__main__':
    abc173_e()