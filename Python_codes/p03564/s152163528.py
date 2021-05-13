from math import log2
n = int(input())
k = int(input())
temp = min(int(log2(k)) + 1, n)
print(2 ** temp + k * (n - temp))