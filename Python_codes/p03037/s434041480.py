import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, m = inintm()

min_id = 10**5+1
max_id = 0

for _ in range(m):
    l, r = inintm()
    min_id = min(min_id, r)
    max_id = max(max_id, l)

print(max(0, min_id-max_id+1))