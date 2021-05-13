import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, m, c = inintm()
B = inintl()
ans = 0

for i in range(n):
    A = inintl()
    point = 0
    for j in range(m):
        point += A[j]*B[j]
    point += c
    if point > 0:
        ans += 1

print(ans)