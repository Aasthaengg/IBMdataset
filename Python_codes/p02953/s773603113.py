import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
H = inintl()

h = H[0]

for i in range(1,n):
    if H[i]+1 < h:
        print("No")
        exit()
    if H[i] > h:
        h = H[i]

print("Yes")
