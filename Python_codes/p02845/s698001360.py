p = 10**9+7
N = int(input())
A = list(map(int,input().split()))
C = {i:0 for i in range(N)}
C[-1] = 3
cnt = 1
for i in range(N):
    a = A[i]
    cnt = (cnt*(C[a-1]-C[a]))%p
    C[a] += 1
print(cnt)