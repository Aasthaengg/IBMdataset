P, Q, R = list(map(int, input().split()))

A = P + Q
B = P + R
C = Q + R
ans = min(A, B, C)
print(ans)