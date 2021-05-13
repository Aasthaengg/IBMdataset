import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
k = inint()
X = inintl()

ans = 0

for x in X:
    ans += 2*min(x,abs(x-k))

print(ans)