## C - Energy Drink Collector
N, M = map(int, input().split())
val = []
for n in range(N):
    val.append( list(map(int, input().split())) )
val = sorted(val, reverse=False, key=lambda x: x[0])
ans = 0
for n in range(N):
    if val[n][1] >= M:
        ans += val[n][0] * M
        break
    else:
        ans += val[n][0] * val[n][1]
        M -= val[n][1]
print(ans)