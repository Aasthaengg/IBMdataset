import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = 1
for i in a:
    if i == m:
        m += 1
if m == 1:
    print(-1)
    exit(0)
print(1+n-m)