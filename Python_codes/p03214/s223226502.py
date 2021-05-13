import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))

m = sum(A) / n
ans = -1
mi = float("inf")
for i in range(n):
    if abs(m - A[i]) < mi:
        ans = i
        mi = abs(m - A[i])
print(ans)