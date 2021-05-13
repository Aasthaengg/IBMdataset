import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
a = sorted(na())
x = [[0]*n for _ in range(30)]
 
if n%3:
    if max(a):
        print("No")
    else:
        print("Yes")
else:
    m = n//3
    if a[0] == a[m-1] and a[m] == a[2*m-1] and a[2*m] == a[3*m-1] and a[0]^a[m] == a[2*m]:
        print("Yes")
    else:
        print("No")