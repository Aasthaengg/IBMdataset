N, A, B = [int(_) for _ in input().split()]
d = B - A
if d % 2:
    t1 = N - B + 1
    ans = t1 + (N - (A + t1)) // 2
    t2 = A
    ans = min(ans, t2 + (B - t2 - 1) // 2)
    print(ans)
else:
    print(d // 2)
