from sys import stdin
N = int(stdin.readline().rstrip())
A = [0] * N
for i in range(N):
    A[i] = int(stdin.readline().rstrip())

if A[0] != 0:
    print(-1)
else:
    ans = 0
    for j in range(N-1):
        if A[j]+1 == A[j+1]:
            ans += 1
        else:
            ans += A[j+1]
        if A[j+1] - A[j] > 1:
            ans = -1
            break
    print(ans)