Z = list(map(int, input().split()))
ans = 10 ** 18
for i in range(3):
    a, b, c = Z[i % 3], Z[(i + 1) % 3], Z[(i + 2) % 3]
    # print(a, b, c)
    left = c // 2
    right = c - left
    ans = min(ans, abs(left - right) * a * b)

print(ans)
