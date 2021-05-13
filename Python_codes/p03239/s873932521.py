import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, t = map(int, readline().split())
cost = 9999
for i in range(n):
    inpt = list(map(int, readline().split()))
    if inpt[1] <= t:
        cost = min(cost, inpt[0])
print(cost if cost != 9999 else 'TLE')
