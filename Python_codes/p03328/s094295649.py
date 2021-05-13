a, b = list(map(int, input().split()))
print(sum([i for i in range(1, b - a + 1)] + [-b, ]))