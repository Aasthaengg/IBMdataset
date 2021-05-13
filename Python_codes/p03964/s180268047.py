def ceil(a, b):
    return a//b+(1 if a % b else 0)


n = int(input())
x, y = 1, 1
for _ in range(n):
    t, a = [int(i) for i in input().split()]
    k = max(ceil(x, t), ceil(y, a))
    x, y = t * k, a * k
print(x+y)
