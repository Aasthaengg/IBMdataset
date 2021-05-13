import numpy as np

n = int(input())
def solve(n):
    f = [float('inf') for _ in range(n+1)]
    f[0] = 0
    for i in range(1, n+1):
        f[i] = f[i-1] + 1
        k = 6
        l = 9
        while k <= i:
            f[i] = min(f[i], f[i-k] + 1)
            k *= 6
        while l <= i:
            f[i] = min(f[i], f[i-l] + 1)
            l *= 9
    print(f[n])
solve(n)