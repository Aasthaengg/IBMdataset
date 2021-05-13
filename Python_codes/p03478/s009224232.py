def s(x):
    if x <= 9:
        return x
    else:
        return x % 10 + s(x // 10)


n, a, b = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    if a <= s(i) <= b:
        ans += i
print(ans)
