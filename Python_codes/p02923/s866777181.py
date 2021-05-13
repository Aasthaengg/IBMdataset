import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instr = lambda: sys.stdin.readline()
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
H = inintl()

ans = 0
cnt = 0
prev = H[0]

for i in range(1,n):
    if H[i] <= prev:
        cnt += 1
        prev = H[i]
    else:
        if cnt > ans:
            ans = cnt
        cnt = 0
        prev = H[i]

if cnt > ans:
    ans = cnt

print(ans)