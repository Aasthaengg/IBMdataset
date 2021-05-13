import sys
#sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for i in range(n):
    d[i] = 0

for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    d[a] += 1
    d[b] += 1

for v in d.values():
    if v%2 != 0:
        print('NO')
        exit()
else:
    print('YES')
