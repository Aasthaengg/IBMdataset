def ranksum(x):
    return sum([int(i) for i in str(x)])

n = int(input())

ans = 10 ** 6
for i in range(1, n):
    a, b = i, n - i
    ans = min(ans, ranksum(a) + ranksum(b))

print(ans)