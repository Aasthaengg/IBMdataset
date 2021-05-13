import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
d = sorted(LI())
m = I()
t = sorted(LI())

j = 0
for i in range(m):
    while t[i] != d[j]:
        j += 1
        if j == n:
            print('NO')
            exit(0)
    j += 1
print('YES')