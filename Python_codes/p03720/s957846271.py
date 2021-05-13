n, m = map(int, input().split())
RD = list(list(map(int, input().split())) for _ in range(m))
for i in range(1, n + 1):
    ans = 0
    for j in RD:
        ans += j.count(i)
    print(ans)