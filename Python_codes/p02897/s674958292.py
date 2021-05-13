n = int(input())
print(len([i for i in range(1, n + 1) if i %2 == 1]) / n)