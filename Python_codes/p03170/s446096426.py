def main():
    n, k = map(int, input().split())
    a = tuple(map(int, input().split()))

    dp = [0] * (k + 1)  # 石がi個で手番が回ってきたら勝てる：1、負ける：0
    for i1 in range(1, k + 1):  # i1：手番が回ってきた時点の石の残数。残数１から始めてｋまでみる。
        for i2 in range(n):
            if i1 - a[i2] >= 0:  # i1-a[i2]がマイナスだと(スライスにより)意図しない値を見てしまうのでパス。
                if dp[i1 - a[i2]] == 0:  # 相手の負けになるようにできるなら、こちらが勝てる。
                    dp[i1] = 1
    if dp[k] == 1:
        print('First')
    else:
        print('Second')


if __name__ == '__main__':
    main()
