n, k = [int(input()) for _ in range(2)]
x = 1
for _ in range(n):
    if x <= k:
        x *= 2
    else:
        x += k
print(x)
