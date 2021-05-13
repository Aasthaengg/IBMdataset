# https://atcoder.jp/contests/apc001/tasks/apc001_b

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
t = sum(b) - sum(a)
pos = 0
neg = 0
for i in range(n):
    d = a[i] - b[i]
    if d > 0:
        pos += d
    elif d < 0:
        neg += -1 * d // 2
if pos <= neg:
    print('Yes')
else:
    print('No')