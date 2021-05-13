N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0

for a in range(K + 1):
    for b in range(K - a + 1):

        # a+b>Nとなるような操作は実現不可能
        if a + b > N:
            continue

        # 左からa個、右からb個取り出す
        get = []
        get += V[:a]
        get += list(reversed(V))[:b]
        # (a+b)回操作した時点でのスコア
        tmp = sum(get)

        # まだ操作出来るなら、負の数を取り除く
        get.sort()
        for i in range(min(K - a - b, len(get))):
            if get[i] < 0:
                tmp += -get[i]
        ans = max(ans, tmp)

print(ans)
