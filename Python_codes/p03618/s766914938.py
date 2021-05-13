import sys
input = sys.stdin.readline

from collections import Counter

A = input().rstrip()

f = lambda x: (x+1)*x//2
answer = f(len(A)) - sum(f(x) for x in Counter(A).values()) + 1

print(answer)