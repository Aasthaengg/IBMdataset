K, A, B = map(int, input().split())

x = (K - (A - 1)) // 2 * (B - A) + A
if (K - (A - 1)) % 2 != 0:
    x += 1

print(max(x, K + 1))
