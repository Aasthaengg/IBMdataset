import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a, b, k = inintm()

for i in range(a,min(b, a+k-1)+1):
    print(i)
for i in range(max(a+k, b-k+1), b+1):
    print(i)