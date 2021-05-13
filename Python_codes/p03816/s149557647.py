import sys
input = sys.stdin.readline
 
N = int(input())
A = [int(x) for x in input().split()]

cnt = 0

from collections import Counter

c = Counter(A)

for i in c.values():
    if i > 1:
        cnt += i - 1

print(N - (cnt + int(cnt % 2 != 0)))