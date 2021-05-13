N, C, K = map(int, input().split())
T = sorted(map(int, (input() for _ in range(N))))
ans = 0
count = 0
bus = None
for t in T:
    tk = t + K
    if bus is None or bus < t or count + 1 > C:
        bus = tk
        count = 0
        ans += 1
    count += 1
print(ans)
