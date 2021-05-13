K, X = map(int, input().split())


for i in range(-1000000, 2000000, 1):
    if i > X - K and i < X + K:
        print(i)