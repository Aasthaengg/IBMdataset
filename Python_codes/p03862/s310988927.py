n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [i for i in a]
b[0] = min(b[0], x)
for i in range(1, n):
    if b[i-1] + b[i] > x:
        b[i] = x - b[i-1]
print(sum(a) - sum(b))