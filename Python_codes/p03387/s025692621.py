A, B, C = map(int, input().split())
D = max(A, B, C)
S = sum([A, B, C])
print((D * 3 - S) // 2 if D % 2 == S % 2 else ((D + 1) * 3 - S) // 2)