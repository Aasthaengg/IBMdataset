import sys,collections,random,math;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

n = I()
t = I()
if t != 0:
    print(-1)
    exit()
sums = 0
for i in range(n-1):
    c = I()
    if c-t > 1 or c > i+1:
        print(-1)
        exit()
    if c-t != 1:
        sums += t
        s = 0
    if i == n-2:
        sums += c
    t = c
print(sums)