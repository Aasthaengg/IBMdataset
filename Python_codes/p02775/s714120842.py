import sys

def resolve(in_):
    dp0 = [1 << 60] * 1000100
    dp1 = [1 << 60] * 1000100
    zero = ord(b'0')
    dp0[0] = 0
    dp1[0] = 2

    for i, v in enumerate(in_.read().rstrip()):
        v -= zero

        # ちょうど支払う。おつりなし。
        dp0[i + 1] = min(dp0[i] + v, dp1[i] + v)

        # 前の桁の支払い枚数に 1 を加えてお釣りを払うのと、
        # 前の桁で多く払ってあるのでお釣りの払い出しの継続の二通り
        dp1[i + 1] = min(dp0[i] + 1 + 10 - v, dp1[i] + 9 - v)
    else:
        i += 1


    return min(dp0[i], dp1[i])


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
