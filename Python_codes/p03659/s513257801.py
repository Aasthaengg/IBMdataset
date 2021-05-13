n = int(input())
a = list(map(int, input().split()))
total = sum(a)
limit = 10**9 + 10**9
b = 0
for i in a[:-1]:
    b += i + i
    diff = abs(total - b)
    if limit > diff:
        limit = diff
print(limit)