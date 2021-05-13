nm = list(map(int, input().split()))

ans = 0

for n in nm:
    ans += (n * (n - 1)) // 2

print(ans)
