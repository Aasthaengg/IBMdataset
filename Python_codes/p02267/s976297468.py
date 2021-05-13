import sys

n = int(sys.stdin.readline())
S = [int(x) for x in sys.stdin.readline().split()]
q = int(sys.stdin.readline())
T = [int(x) for x in sys.stdin.readline().split()]

count = 0
for t in T:
    for s in S:
        if s == t:
            count += 1
            break

print(count)
