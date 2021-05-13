import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
print(n*(n-1)//2-n//2)

for i in range(n):
    a = n-1-i if n%2 == 0 else n-2-i
    for j in range(i+1,n):
        if j != a:
            print(i+1,j+1)