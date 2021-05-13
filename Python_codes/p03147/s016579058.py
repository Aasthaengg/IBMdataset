input()
h = list(map(int, input().split()))
h.append(-1)
ans = 0
state = "up"
for i, j in zip(h[:-1], h[1:]):
    if state == "up" and i > j:
        ans += i
        state = "down"
    if state == "down" and i < j:
        ans -= i
        state = "up"
print(ans)