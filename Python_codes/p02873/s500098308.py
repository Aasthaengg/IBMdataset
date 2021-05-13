S = list(input().replace("><", ">,<").split(","))
ans = 0
for s in S:
    n = s.count("<")
    m = s.count(">")
    ans += (n * (n - 1)) // 2 + (m * (m - 1)) // 2 + max(n, m)
print(ans)
