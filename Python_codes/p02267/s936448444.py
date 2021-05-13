import sys

n = int(sys.stdin.readline())
s = [int(x) for x in sys.stdin.readline().split()]
q = int(sys.stdin.readline())
t = [int(x) for x in sys.stdin.readline().split()]
cnt = 0

for i in t:
    if i in s:
        cnt += 1

print(cnt)