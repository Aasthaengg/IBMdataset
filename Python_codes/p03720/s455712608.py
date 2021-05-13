import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, m = inintm()

city = [0]*(n+1)

for _ in range(m):
    a, b = inintm()
    city[a] += 1
    city[b] += 1

for c in range(1,n+1):
    print(city[c])
