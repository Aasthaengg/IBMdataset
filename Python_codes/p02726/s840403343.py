n, x, y = map(int, input().split())
L1 = x - 1
L2 = n - y
C = y - x + 1
for k in range(1, n):
    ans = 0
    if 2 * k == C:
        ans += C // 2
    elif 2 * k < C:
        ans += C
    for L in L1, L2:
        if C % 2 == 0 and 0 < k - C // 2 <= L:
            ans += 1
        ans += max(0, (min(L, k-1) - max(1, k - (C - 1) // 2) + 1) * 2) + (L >= k)
    ans += max(0, L1 + L2 + 2 - k) - sum(k <= x for x in [L1, L2+1, L2, L1+1]) + (k == 1)
    print(ans)