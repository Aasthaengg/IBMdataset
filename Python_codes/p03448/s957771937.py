import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a = inint()
b = inint()
c = inint()
x = inint()

ans = 0

for i in range(a+1):
    for k in range(b+1):
        for j in range(c+1):
            if 500*i + 100*k + 50*j == x:
                ans += 1

print(ans)