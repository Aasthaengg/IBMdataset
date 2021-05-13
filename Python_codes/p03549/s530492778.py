n, m = map(int, input().split())
k = n - m
one = m * 1900 + k * 100
print(2**m * one)