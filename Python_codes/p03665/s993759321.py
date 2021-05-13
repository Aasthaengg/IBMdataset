import math
n, p, *a = map(int, open(0).read().split())


def c(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


memo = [0, 0]
for i in range(n):
    memo[a[i] % 2] += 1
# p == 0


ans = 0
if p == 0:
    for i in range(0, memo[1] + 1, 2):
        ans += c(memo[1], i) * pow(2, memo[0])
else:
    for i in range(1, memo[1] + 1, 2):
        ans += c(memo[1], i) * pow(2, memo[0])
# p == 1
print(ans)
