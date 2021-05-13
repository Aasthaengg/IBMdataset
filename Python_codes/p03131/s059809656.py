K, A, B = [int(_) for _ in input().split()]

upbis = 0
k = K - A + 1
if B > A:
    upbis = A + (k // 2) * (B-A) + (k % 2)

print(max(1+K, upbis))