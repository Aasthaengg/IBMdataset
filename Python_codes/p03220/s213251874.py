import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
t, a = inintm()
H = inintl()

diff = 10**6
ans = 0

for i in range(n):
    if abs(a-(t + -0.006*H[i])) < diff:
        diff = abs(a-(t + -0.006*H[i]))
        ans = i+1

print(ans)