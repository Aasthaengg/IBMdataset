import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0
if A[0] != 0:
    ans = -1
else:
    for i in range(1, N)[::-1]:
        d = A[i] - A[i-1]
        if d > 1:
            ans = -1
            break
        if d == 1:
            ans += 1
        else:
            ans += A[i]
print(ans)


