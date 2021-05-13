import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

x = inint()

ans = 0

for i in range(1,10**5):
    if i*(i+1)/2 >= x:
        print(i)
        break

