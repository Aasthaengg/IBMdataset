from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(_) for _ in stdin.readline().rstrip().split()]
ans = 0
for i in range(1, N):
    if A[i-1] == A[i]:
        A[i] = -1
        ans += 1
print(ans)