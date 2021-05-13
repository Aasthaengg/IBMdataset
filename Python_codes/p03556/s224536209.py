n = int(input())
m = int(n ** 0.5 + 3)
for i in range(m):
    if i ** 2 > n:
        print((i - 1) ** 2)
        break