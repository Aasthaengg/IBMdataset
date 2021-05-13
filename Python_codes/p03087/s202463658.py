n, q = map(int, input().split())

s = input()

count = [0] * n

for i in range(1, n):
    if s[i-1] == 'A' and s[i] == 'C':
        count[i] += 1

from itertools import accumulate

accum = list(accumulate(count))

for _ in range(q):
    l, r = map(int, input().split())
    print(accum[r-1] - accum[l-1])