#!/usr/bin/env python3
# input
X, K, D = map(int, input().split())
DIV = (X + K * D) // (2 * D)

if X + K * D < 0:
    ans = -(X + K * D)
elif X - K * D > 0:
    ans = X - K * D
else:
    ans = min(X + K * D - DIV * D * 2, -(X + K * D - (1 + DIV) * D * 2))
print(ans)
