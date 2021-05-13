N = int(input())
p = 1
m = int(1e+9 + 7)
for i in range(1, N + 1):
    p = p * i
    if p > m:
        p = p % m
print(p)