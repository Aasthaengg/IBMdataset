import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X = int(input())
fac = {}
fac[0] = 0
for i in range(1, 50000):
    fac[i] = fac[i-1]+i
    if fac[i]>=10**9:
        break

for i in range(1, 50000):
    f = fac[i]
    if f>=X:
        print(i)
        break