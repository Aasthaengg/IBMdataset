A, B, C = map(int, input().split())
abc_max = max(A, B, C)
if (A + B + C) % 2 == abc_max % 2:
    print((3 * abc_max - (A + B + C)) // 2)
else:
    print((3 * (abc_max + 1) - (A + B + C)) // 2)
