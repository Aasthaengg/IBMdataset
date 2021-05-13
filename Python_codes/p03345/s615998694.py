A, B, C, K = map(int, input().split())
if K % 2 == 0:
    r = A - B
else:
    r = B - A
print(r if r <= 10**18 else "Unfair")
