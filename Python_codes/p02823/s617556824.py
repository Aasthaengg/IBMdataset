N, A, B = map(int, input().split())

if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    # Aが左に到着
    ans1 = 0
    ans1 += A - 1 + 1
    a = 1
    b = B - A
    ans1 += (b - a) // 2

    # Bが右に到着
    ans2 = 0
    ans2 += N - B + 1
    a = A + (N - B + 1)
    b = N
    ans2 += (b - a) // 2

    ans = min(ans1, ans2)
    print(ans)
