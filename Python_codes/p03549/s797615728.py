from math import pow

N, M = map(int, input().split(' '))

tries = int(pow(2, M))
time_per_try = 1900 * M + 100 * (N - M)

print(tries * time_per_try)
