from math import ceil

n, m = map(int, input().split())

left = 1
prob = 0
ac = 0.5 ** m
for i in range(1, 10000):
    prob += i * left * ac
    left -= left * ac

ans = (100 * (n - m) + 1900 * m) * prob
ans = ceil(ans)
print(ans)
