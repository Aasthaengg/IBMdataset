# -*- coding: utf-8 -*-
n, m, d = map(int, input().split())
# n2cnt = [[i, 1] for i in range(1, n + 1)]
# beauty = 0

# for _ in range(m - 1):
#     beauty *= 2

#     for i, cnt in n2cnt:
#         if i - d > 0:
#             beauty += cnt
#         if i + d <= n:
#             beauty += cnt

#     n2cnt = [[i, cnt * n] for i, cnt in n2cnt]

# print(beauty / sum([cnt for i, cnt in n2cnt]))
if d == 0:
    p = n
else:
    p = (n - d) * 2
q = n ** 2 - p
print((1 * p + 0 * q) / n**2 * (m - 1))
