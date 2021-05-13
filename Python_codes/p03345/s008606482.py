A, B, C, K = map(int, input().split())
ans = B - A if K % 2 == 1 else A - B
print(ans if abs(ans) <= 10 ** 18 else "Unfair")

