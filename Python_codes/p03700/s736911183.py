import sys
input = lambda: sys.stdin.readline().rstrip()
n, a, b = map(int, input().split())
h = []
for _ in range(n):
    h.append(int(input()))

def solve(e):
    cnt = 0
    for i in h:
        if i<=b*e:
            continue
        cnt += (i-b*e+a-b-1)//(a-b)
    return cnt<=e

ok = 10**9
ng = 0
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(ok)