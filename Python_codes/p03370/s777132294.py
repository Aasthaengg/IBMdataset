import sys
n,x = map(int, sys.stdin.readline().rstrip("\n").split())
minm = 100000
summ = 0
for _ in range(n):
    m = int(sys.stdin.readline().rstrip("\n"))
    summ += m
    minm = min(minm,m)
print(n+(x-summ)//minm)