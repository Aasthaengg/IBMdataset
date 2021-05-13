# -*- coding: utf-8 -*-
from collections import deque

n = int(input())
a = list(map(int, input().split()))

positives = deque(sorted(a))
negatives = deque([positives.popleft()])
while len(positives) > 1:
    if positives[0] < 0:
        negatives.append(positives.popleft())
    else:
        break

# print M
print(sum(positives) - sum(negatives))

while len(positives) > 1:
    y = positives.popleft()
    x = negatives.pop()
    print(x, y)
    negatives.append(x - y)

x = positives.popleft()

while len(negatives) > 0:
    y = negatives.pop()
    print(x, y)
    x = x - y