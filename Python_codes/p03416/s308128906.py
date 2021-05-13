a, b = map(int, input().split())
ans = 0
for q in range(a, b + 1):
    if q == int(str(q)[::-1]):
        ans += 1
print(ans)