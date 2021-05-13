N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x:x[0])
ans = 0
for a, b in AB:
    if b <= M:
       ans += a * b
       M -= b
    else:
        ans += a * M
        break
    if M == 0:
        break
print(ans)