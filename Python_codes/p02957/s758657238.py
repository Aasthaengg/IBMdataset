a, b = list(map(int, input().split()))

if (a + b) % 2 == 1:
    print("IMPOSSIBLE")
else:
    print((a + b) // 2)