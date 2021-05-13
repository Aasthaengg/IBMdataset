import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
A = inintl()

c = 0
cnt = [0]*n

for i in range(n):
    A[i] -= 1

for i in range(n):
    cnt[A[i]] += 1

def combinations(n):
    return n*(n-1)//2

for i in range(n):
    c += combinations(cnt[i])

for i in range(n):
    ans = c
    ans -= combinations(cnt[A[i]])
    ans += combinations(cnt[A[i]]-1)
    print(ans)

