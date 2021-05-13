n = int(input())
H = list(map(int, input().split()))

ans = 0
now = 0

for h in H:
    if h <= now:
        now = h
    else:
        ans += h - now
        now = h

print(ans)
