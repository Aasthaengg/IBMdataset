# ABC 082: A – Round Up the Mean
a, b = [int(s) for s in input().split()]
print((a + b) //  2 if (a + b) % 2 == 0 else (a + b) // 2 + 1)