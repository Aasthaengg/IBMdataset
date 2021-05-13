def main():
    T1, T2 = list(map(int, input().split()))
    A1, A2 = list(map(int, input().split()))
    B1, B2 = list(map(int, input().split()))
    # 青木君を基準にした高橋君の位置を追い、0に何回ぶつかるかを調べる
    V1, V2 = A1 - B1, A2 - B2
    if V1 == 0 or V2 == 0 or V1 * V2 > 0:
        print(0)
        return
    # この後は V1 * V2 < 0
    d1, d2 = V1 * T1, V2 * T2
    d12 = d1 + d2
    if d1 * d12 > 0:
        print(0)
    elif d12 == 0:  # d1 * d12 == 0
        print('infinity')
    else:  # d1 * d12 < 0
        cnt = 0
        # d1で0に達する
        cnt += abs(d1) // abs(d12)
        # d2で0に達する
        cnt += 1 + (abs(d1) - 1) // abs(d12)
        print(cnt)


if __name__ == '__main__':
    main()
