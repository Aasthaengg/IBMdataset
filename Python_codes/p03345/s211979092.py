a, b, c, k = list(map(int, input().split()))

if a == b == c:
    print(0)
    exit()

if abs(a - b) >= 1e18:
    print("Unfair")
    exit()

if k % 2 == 0:
    print(a - b)
else:
    print((a - b) * -1)
