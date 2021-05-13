n = int(input())
k = int(input())
xs = map(int, input().split())

ans = 0
for x in xs:
    ans += 2 * min(x, abs(k - x))

print(ans)
