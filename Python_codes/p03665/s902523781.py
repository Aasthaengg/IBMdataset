# https://atcoder.jp/contests/agc017/tasks/agc017_a

from math import factorial
n, p = map(int, input().split())

nums = [int(i) for i in input().split()]

odd = 0
even = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
ans = 0
if p == 0:
    e = 2 ** even
    o = 0
    for i in range(0, odd + 1, 2):
        o += factorial(odd) // (factorial(odd - i) * factorial(i))
    ans += e * o
elif p == 1:
    e = 2 ** even
    o = 0
    for i in range(1, odd + 1, 2):
        o += factorial(odd) // (factorial(odd - i) * factorial(i))
    ans += e * o
print(ans)