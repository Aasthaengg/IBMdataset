import sys
input = lambda: sys.stdin.readline().rstrip()

a, b, m = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
xyc = []
for _ in range(m):
    xyc.append([int(x) for x in input().split()])
ans = min(A) + min(B)
for i in range(m):
    x, y, c = xyc[i]
    temp = A[x - 1] + B[y - 1] - c
    ans = min(ans, temp)
print(ans)