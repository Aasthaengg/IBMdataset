X = int(input())

for i in range(1, 50000):
    n = i * (i + 1) / 2
    if n >= X:
        print(i)
        break