n, m = map(int,input().split())
store = [list(map(int,input().split())) for _ in range(n)]
store = sorted(store, key=lambda x: x[0])

i = 0
ans = 0
while True:
    if store[i][1] < m:
        ans += store[i][0]*store[i][1]
        m -= store[i][1]
        i += 1
    else:
        ans += m*store[i][0]
        break
print(ans)
