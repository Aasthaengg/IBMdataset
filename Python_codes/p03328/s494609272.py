import sys
sys.setrecursionlimit(100000) 
def f(n):
    if n == 0:
        return 0
    else:
        return n + f(n-1)
a, b = list(map(int,input().split()))
i1 = 1
i2 = 2
while True:
    if b - a == f(i2) - f(i1):
        break
    i1 += 1
    i2 += 1
print(f(i1) -a)