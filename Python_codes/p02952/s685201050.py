n = int(input())
ans = 0
for i in range(1, n+1):
    if 0 < i < 10 or 99 < i < 1000 or 9999 < i < 100000:
        ans += 1
print(ans)
