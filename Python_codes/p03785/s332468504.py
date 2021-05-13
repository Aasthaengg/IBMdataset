n, c, k = map(int, input().split())
times = []
for _ in range(n):
    t = int(input())
    times.append((t, t+k))
times.sort(key=lambda x: x[1])

ans = 0
x = 0
capacity = 0
for L, R in times:
    if L <= x:
        if c == capacity:
            capacity = 1
            ans += 1
            x = R
        else:
            capacity += 1
    else:
        x = R
        ans += 1
        capacity = 1
print(ans)