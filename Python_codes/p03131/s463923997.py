K, A, B = map(int, input().split())

if B - A <= 2:
    print(K + 1)
else:
    time = max(0, (K - (A - 1)) // 2)
    ans = A + (B - A) * time
    if (K - (A - 1)) % 2 == 1:
        ans += 1
    print(ans)


