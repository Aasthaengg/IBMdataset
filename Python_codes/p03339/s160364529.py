import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
s = readline().decode().rstrip()

cost = [0]*n
cost[0] = s[1::].count('E')
if s[0] == 'W':
    cost[1] += 1

for i in range(1, n):
    if s[i] == 'E':
        cost[i] += cost[i - 1] - 1
    else:
        cost[i] += cost[i - 1]
        if i < n - 1:
            cost[i + 1] += 1

print(min(cost))