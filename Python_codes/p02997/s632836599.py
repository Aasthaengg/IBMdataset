from itertools import combinations

n, k = map(int, input().split())
star = []
max_k = (n - 1) * (n - 2) // 2
delta = max_k - k
cnt = 0
if k <= max_k:
    ans = []
    for i in range(2, n + 1):
        star.append((1, i))
        cnt += 1

    if delta > 0:
        kumiawase = list(combinations(range(2, n+1), 2))
        for j in range(delta):
            kumi = kumiawase[j]
            star.append(kumi)
            cnt += 1
    print(cnt)
    for pair in star:
        print(*pair, sep=" ")
else:
    print(-1)
