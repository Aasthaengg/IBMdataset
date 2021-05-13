def abc175_c_2():
    x, k, d = map(int, input().split())

    def solve(x, k, d):
        # Xを絶対値でプラスの値にし、0に近づける問題に置き換える
        x = abs(x)

        # (x // d)は0の手前まで移動するのに必要な回数。kの方が小さい場合はk回移動してしまえばよい
        if k < (x // d):
            return x - (k * d)
        # kのほうが大きい場合はそこから数回移動が必要
        else:
            # xからとりあえずx//d回は移動してOK
            current_x = x - d * (x // d)
            k = k - (x // d)

            # 結局ここをfor文で探索すると時間がかかるので終わらない。(10**30回とか探索しちゃう。)
            if (k % 2) == 0:
                # 残りの移動回数が偶数回なら移動を繰り返してその場所に戻ってくる
                return current_x
            else:
                # 奇数回の場合、偶数回移動を繰り返した後、もう一回だけ移動する。
                # この時、current_xは0以上なので、マイナス方向に動けばOK
                return abs(current_x - d)

    ans = solve(x, k, d)
    print(ans)

if __name__ == '__main__':
    abc175_c_2()