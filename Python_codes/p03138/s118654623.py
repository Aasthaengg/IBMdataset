import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,k = na()
a = na()
b = [0]*40

for i in a:
    for j in range(40):
        if (i>>j) & 1:
            b[j]+=1

ans = 0
for i in range(40)[::-1]:
    if b[i] < n/2:
        ans += 1<<i
    if ans > k:
        ans -= 1<<i

bns = 0
for i in a:
    bns += i^ans

print(bns)