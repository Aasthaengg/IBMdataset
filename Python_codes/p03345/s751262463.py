A, B, C, K = map(int, input().split())
d = A - B if K % 2 == 0 else B - A
print(d if abs(d) <= 10**18 else "Unfair")