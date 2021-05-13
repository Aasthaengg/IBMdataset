
def resolve():
    N, K = map(int, input().split())

    # Kの倍数である数値の個数を数える
    a = 0
    for i in range(1, N + 1):
        if i % K == 0:
            a += 1

    # 余りがKの半分となる数値の個数を数える
    b = 0
    for i in range(1, N + 1):
        if i % K == K // 2:
            b += 1

    # 全ての要素がKの倍数の場合を足す
    ans = a * a * a
    if K % 2 == 0:
        # 全ての要素がK/2の場合を足す
        ans += b * b * b

    print(ans)


if __name__ == "__main__":
    resolve()
