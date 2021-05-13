import math
n, m, d = map(int, input().split())

# sum = 0
# for i in range(1,n+1):
#     cnt = 0
#     if i + d <= n:
#         cnt += 1
#     if i - d > 0:
#         cnt += 1
#     sum += cnt / n / n * (m-1)

if d != 0:
    print(2 * (n - d - d) * (m-1) / n / n + 2*d * (m-1) / n / n)
else:
    print((m-1)/n)