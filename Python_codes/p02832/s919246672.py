import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

t = 1

s = 0

if t not in a:
    s = -1
else:
    for x in a:
        if x == t:
            t += 1
        else:
            s += 1

print(s)
