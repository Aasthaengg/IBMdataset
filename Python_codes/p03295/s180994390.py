N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
AB.sort()
prev, ans = AB[0][1], 1
for a, b in AB[1:]:
    if prev <= a:
        ans += 1
        prev = b
    else:
        prev = min(prev, b)
print(ans)