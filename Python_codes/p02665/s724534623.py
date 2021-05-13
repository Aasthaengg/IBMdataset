n = int(input())
values = list(map(int, input().split()))

from itertools import accumulate

copy = values[:]
copy.reverse()
acc = list(accumulate(copy))
acc.reverse()

b = 1
total = 1
for i in range(n+1):
    a = values[i]
    bCandidate = b - a
    if bCandidate < 0:
        print(-1)
        exit()
    b = min(2*bCandidate, acc[i] - a)
    total += b
print(total)