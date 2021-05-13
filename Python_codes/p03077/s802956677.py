N = int(input())
times = [int(input()) for _ in range(5)]
bottle_neck = min(times)
print((N + bottle_neck - 1) // bottle_neck + 4)
