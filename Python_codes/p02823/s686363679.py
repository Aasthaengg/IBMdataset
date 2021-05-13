N, A, B = map(int, input().split())

if (B-A) % 2 == 0:
    print((B-A) // 2)
else:
    straight = min(B - 1, N - A)
    wrap = 1 + min(A - 1, N - B) + (B - A) // 2
    print(min(straight, wrap))