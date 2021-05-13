N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = [0] * N
m = -1

for i in range(N-1):
    if i == N-2:
        ans[A[i]-1] = i - m
    elif A[i] != A[i+1]:
        ans[A[i]-1] = i - m
        m = i
for i in range(N):
    print(ans[i])