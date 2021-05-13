K, A, B = map(int, input().split())

if B - A <= 2:
    print(1 + K)
elif A + 1 > K:
    print(1 + K)
else:
    rest = K - A + 1
    b = (rest // 2) * (B - A) + rest % 2 + A
    print(max(1 + K, b))
