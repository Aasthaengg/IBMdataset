N, M = map(int, input().split())
ST = []
for _ in range(M):
    a, b = map(int, input().split())
    ST.append((a, b))

ST.sort(key=lambda x: x[1])

ans = 0
t = 0
for a, b in ST:
    if a >= t:
        t = b
        ans += 1

print(ans)