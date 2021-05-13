n, k = map(int, input().split())
num = sorted([list(map(int, input().split())) for _ in range(n)])

cnt = 0
for a, b in num:
    cnt += b
    if cnt >= k:
        print(a)
        break