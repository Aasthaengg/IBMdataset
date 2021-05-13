from sys import stdin

n = int(stdin.readline().rstrip())
V = [int(v) for v in stdin.readline().rstrip().split()]

V.sort()

now = V[0]

for v in V[1:]:
    now = (now + v)/2

print(now)