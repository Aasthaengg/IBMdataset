n,k = map(int, input().split())

ab = sorted([list(map(int, input().split())) for _ in range(n)])
cnt = 0
for i in ab:
    cnt += i[1]
    if cnt >= k:
        print(i[0])
        exit(0)