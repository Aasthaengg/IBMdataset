from sys import stdin

n = int(stdin.readline().rstrip())
h = [int(x) for x in stdin.readline().rstrip().split()]

nowstep = 0
maxstep = 0

for i in range(n-1, 0, -1):
    if h[i] <= h[i-1]:
        nowstep += 1
    else:
        nowstep = 0
    maxstep = max(maxstep, nowstep)

print(maxstep)