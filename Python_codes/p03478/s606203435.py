N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    total = 0
    buf = i
    for j in range(4, -1, -1):
        division, buf = divmod(buf, 10**j)
        total += division
    if total >= A:
        if total <= B:
            ans += i
print(ans)