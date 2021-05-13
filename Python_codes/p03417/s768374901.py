n, m = [int(i) for i in input().split()]

n = 1 if n < 2 else n - 2
m = 1 if m < 2 else m - 2

print(n * m)