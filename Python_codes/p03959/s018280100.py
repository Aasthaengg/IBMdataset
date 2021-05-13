import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
maxh = [0] * N
if T[0] > A[0] or T[-1] < A[-1]:
    print(0)
    exit()

maxh[0] = -T[0]
for i in range(1, N):
    if T[i-1] == T[i]:
        maxh[i] = T[i]
    else:
        maxh[i] = -T[i]

maxh[-1] = -A[-1]
for i in range(N-1)[::-1]:
    if maxh[i] > 0:
        if A[i] == A[i+1]:
            maxh[i] = min(maxh[i], A[i])
        else:
            if maxh[i] < A[i]:
                print(0)
                exit()
            else:
                maxh[i] = -A[i]
    else:
        if A[i] == A[i+1]:
            if -maxh[i] > A[i]:
                print(0)
                exit()
        else:
            if -maxh[i] != A[i]:
                print(0)
                exit()

ans = 1
mod = 10**9+7
for i in range(N):
    if maxh[i] > 0:
        ans = ans * maxh[i] % mod
print(ans)
