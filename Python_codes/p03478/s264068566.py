n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    s = 0
    for j in range(5):
        m = 10**j
        s += (i // m) % 10
    if a <= s <= b:
        ans += i
print(ans)