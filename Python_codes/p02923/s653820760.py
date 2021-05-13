import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
h = list(map(int, input().split()))
prv = h[0]
ans = 0
c = 0
for i in range(1,n):
    if prv>=h[i]:
        c += 1
    else:
        ans = max(ans, c)
        c = 0
    prv = h[i]
ans = max(ans, c)
print(ans)