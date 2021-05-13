n, k = map(int, input().split())
if k & 1:
    print((n // k) ** 3)
else:
    cnt = n // k
    if n % k >= k // 2:
        print(cnt ** 3 + (cnt + 1) ** 3)
    else:
        print(2 * cnt ** 3)
