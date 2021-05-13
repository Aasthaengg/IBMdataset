import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = int(input())
print(0)
l = input()
r = l
if l == "Vacant":
    exit()

ng,ok = 0,n
while True:
    mid = (ng + ok) // 2
    print(mid)
    q = input()
    if q == "Vacant":
        exit()
    if (q == l) ^ ((mid - ng)%2 == 1):
        ng = mid
        l = q
    else:
        ok = mid
        r = q