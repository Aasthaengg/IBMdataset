K, A, B = map(int, input().split())

if B - A <= 2:
    print(K + 1)
    exit()

x = (K - (A - 1)) // 2 * (B - A) + A
if (K - (A - 1)) % 2 != 0:
    x += 1

print(max(x, K + 1))
