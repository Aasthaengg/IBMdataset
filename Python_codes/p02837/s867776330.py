import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, a, s, h = int(input()), [], [], []
for i in range(n): a.append(int(input())); s.append(list(list(map(int, input().split())) for _ in range(a[i])))
for i in range(2 ** n):
    flag = False
    for j in range(n):
        if (i >> j) & 1:
            for ps in s[j]:
                if (i >> (ps[0]-1) & 1) != ps[1]: flag = True; break
    if not flag: h.append(bin(i)[2:].count('1'))
print(max(h))