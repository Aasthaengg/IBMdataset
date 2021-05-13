import sys
input = sys.stdin.readline

N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b
ans = 0
for i in range(N-1,-1,-1):
    A[i] += ans
    if A[i]%B[i] != 0:
        ans += B[i]-(A[i]%B[i])
print(ans)
