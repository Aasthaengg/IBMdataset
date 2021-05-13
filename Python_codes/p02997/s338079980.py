n, k = map(int, input().split())
# 最大ケース・うに: (n - 1) * (n - 2) // 2
# 最小ケース・完全グラフ: 0

if k <= (n - 1) * (n - 2) // 2:
    # つくれる
    hen = []
    for i in range(2, n + 1):
        hen.append((1, i))
    m = (n - 1) * (n - 2) // 2 - k
    while m:
        for i in range(2, n + 1):
            for j in range(i + 1, n + 1):
                hen.append((i, j))
                m -= 1
                if m == 0:
                    break
            if m == 0:
                break
    print(len(hen))
    for a, b in hen:
        print(a, b)

else:
    print(-1)
