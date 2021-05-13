# 容器2に残る水の量を求める

A, B, C = map(int, input().split())

if A <= (B + C):
    print((B + C) - A)
else:
    print(0)
