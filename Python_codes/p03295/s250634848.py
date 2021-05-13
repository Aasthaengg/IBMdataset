n, m = map(int, input().split())
AB = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: x[1])
last_b, cnt = 0, 0
for a, b in AB:
    if last_b < a:
        last_b = b - 1
        cnt += 1
print(cnt)