import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def F(n: int):
    i = 2
    while i * i <= n:
        while n % i == 0: yield i; n //= i
        i += 1
    if n != 1: yield n

(a, b), c = map(lambda x: set(F(int(x))), input().split()), 0
for i in a: c += 1 if i in b else 0
print(c + 1)