import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a, b = inintm()

ans = 0

for i in range(a,b+1):
    if str(i) == str(i)[::-1]:
        ans += 1

print(ans)
