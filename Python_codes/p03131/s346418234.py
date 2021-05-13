K, A, B = map(int, input().split())
if A + 2 >= B:
    ans = 1 + K
else:
    L = K - A + 1
    ans = (L // 2) * (B - A) + A
    if L % 2 == 1:
        ans += 1
print(ans)