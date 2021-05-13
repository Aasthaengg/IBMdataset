import sys

input = sys.stdin.readline

N,M = map(int,input().split())

sel = [0] * N

for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    sel[a] += 1
    sel[b] += 1

ans = "YES"
for j in range(N):
    if sel[j] % 2 == 1:
        ans = "NO"

print(ans)
