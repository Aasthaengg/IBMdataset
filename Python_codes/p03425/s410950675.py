from sys import stdin
def input():
    return stdin.readline().strip()
 
n = int(input())
m, a, r, c, h = 0, 0, 0, 0, 0
for _ in range(n):
    i = input()
    i = i[0]
    if i == 'M':
        m += 1
    elif i == 'A':
        a += 1
    elif i == 'R':
        r += 1
    elif i == 'C':
        c += 1
    elif i == 'H':
        h += 1
 
ans = 0
from itertools import combinations
for i in combinations([m, a, r, c, h], 3):
    i, j, k = i
    ans += i * j * k
print(ans)