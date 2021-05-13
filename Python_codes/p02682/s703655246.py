A, B, C, K = map(int, input().split())

ans = 0
if K >= A:
    ans += A
    K -= A
    if K >= B:
        K -= B
        ans -= K
else:
    ans += K

print(ans)
