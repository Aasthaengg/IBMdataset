N = int(input())
A = list(map(int, input().split()))

L, R = [0]*(N+1), [0]*(N+1)
L[N] = R[N] = A[N]
for i in range(N)[::-1]:
    L[i] = A[i] + (L[i+1]+1)//2
    R[i] = A[i] + R[i+1]

if L[0] > 1:
    print(-1)
    exit()

v, ans = 1, 1
for i in range(N):
    v = min((v-A[i])*2, R[i+1])
    ans += v

print(ans)