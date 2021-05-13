import sys
input = sys.stdin.readline
n = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))

B = [[-1] * n for i in range(4)]

B[0][0] = T[0]
B[1][0] = T[0]+1

for i in range(1, n):
    if T[i] == T[i-1]:
        B[0][i] = 1
        B[1][i] = T[i] + 1
    elif T[i] > T[i-1]:
        B[0][i] = T[i]
        B[1][i] = T[i] + 1

B[2][n-1] = A[-1]
B[3][n-1] = A[-1]+1

for i in range(n-2, -1, -1):
    if A[i] == A[i+1]:
        B[2][i] = 1
        B[3][i] = A[i] + 1
    elif A[i] > A[i+1]:
        B[2][i] = A[i]
        B[3][i] = A[i] + 1

# print(B)

ans = 1
mod = 10**9+7
for i in range(n):
    ans = (ans * max(0, min(B[1][i], B[3][i]) - max(B[0][i], B[2][i]))) % mod
print(ans)