N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
ans = 0
i = 0
ab.sort()
while cnt < M:
    tmp = ab[i][1]
    prc = ab[i][0]
    ans += prc * tmp
    cnt += tmp
    i += 1
print(ans - (cnt-M)*prc)