n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)
s = 0
res = float('inf')
for v in a[:-1]:
    s += v
    res = min(res, abs(sum_a - 2 * s))

print(res)