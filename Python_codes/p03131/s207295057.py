K, A, B = [int(_) for _ in input().split()]

if B - A <= 2 or K <= A:
    print(K + 1)
else:
    ans = (K - A + 1) % 2
    N = (K - A + 1) // 2 - 1
    ans += B + (B-A) * N
    print(ans)
