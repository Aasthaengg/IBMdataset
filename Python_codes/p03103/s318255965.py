import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dict1 = {}
for _ in range(n):
    price, b = map(int, input().split())
    if price in dict1:
        dict1[price] += b
    else:
        dict1[price] = b

money_cnt = 0
for price, b in sorted(dict1.items()):
    if b < m:
        m -= b
        money_cnt += price * b
    else:
        money_cnt += price * m
        break
print(money_cnt)