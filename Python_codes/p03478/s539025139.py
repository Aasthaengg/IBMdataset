import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, a, b =  inintm()

ans = 0

for i in range(1,n+1):
    i = str(i)
    s = 0
    for j in range(len(i)):
        s += int(i[j])
    if a <= s <= b:
        ans += int(i)

print(ans)
