import sys
input = sys.stdin.readline

n, h, w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]

ans = 0
for i in range(n):
    if A[i][0] >= h and A[i][1] >= w:
        ans += 1
print(ans)