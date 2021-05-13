from sys import stdin
input = stdin.buffer.readline

n, t = map(int, input().split())

cost = 10000

for _ in range(n):
    c, i = map(int, input().split())
    if i <= t and c < cost:
        cost = c

if cost == 10000:
    print('TLE')
else:
    print(cost)