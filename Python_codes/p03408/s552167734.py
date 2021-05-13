import sys
input = sys.stdin.readline
Pl = []
Mi = []

N = int(input())
for i in range(N):
    Pl.append(input().rstrip('\n'))
M = int(input())
for i in range(M):
    Mi.append(input().rstrip('\n'))

ans = 0
for s in Pl:
    ans = max(ans, Pl.count(s)-Mi.count(s))
print(ans)
