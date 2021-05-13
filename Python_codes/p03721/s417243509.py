n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda i: i[0])
for i in range(n):
    k -= ab[i][1]
    if k <= 0:
        print(ab[i][0])
        exit()
