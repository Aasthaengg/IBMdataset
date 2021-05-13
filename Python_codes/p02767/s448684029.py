import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
X = inintl()

p = 0
min_d = 10**10
ans = 0

for i in range(1,max(X)+1):
    t_d = 0
    for x in X:
        t_d += (x-i)**2
    if t_d < min_d:
        min_d = t_d
        p = i

for x in X:
    ans += (x-p)**2

print(ans)
