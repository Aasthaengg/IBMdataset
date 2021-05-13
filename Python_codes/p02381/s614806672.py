# 10_C
import math

while True:
    n = int(input())
    if n == 0:
        break
    else:
        sigma = 0
        n_list = list(map(int, input().split()))
        avg = sum(n_list) / n
        for i in range(n):
            sigma += (n_list[i] - avg) ** 2
        a = math.sqrt(sigma / n)
        print(abs(a))
