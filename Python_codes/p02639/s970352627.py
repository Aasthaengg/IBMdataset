x = [int(n) for n in input().split(' ')]
for i, n in enumerate(x):
    if n == 0:
        print(i + 1)
