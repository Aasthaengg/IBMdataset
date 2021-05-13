from itertools import accumulate

N = int(input())
a_li = list(map(int, input().split()))
# y = X - x
# |x - y| = |x - (X - x)|
#         = |-X + 2x|
total = sum(a_li)
acc = list(accumulate(a_li))
ans = 10 ** 18
for i in range(N - 1):
    ans = min(ans, abs(acc[i] * 2 - total))
print(ans)
