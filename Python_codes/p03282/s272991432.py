import sys
input = sys.stdin.readline

S=input().strip()
K=int(input().strip())

n = 0
m = 0
for c in S:
    if c != '1':
        m = int(c)
        break
    n += 1
if K <= n:
    print(1)
else:
    print(m)