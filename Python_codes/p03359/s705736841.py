a, b = list(map(int, input().split()))

ans = 0
ans += a - 1

if a <= b:
    ans += 1

print(ans)