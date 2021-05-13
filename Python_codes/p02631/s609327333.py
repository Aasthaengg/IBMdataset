N = int(input())
A = list(map(int, input().split()))

S = 0
for a in A:
    S = S ^ a

ans = [0]*N
for i in range(N):
    ans[i] = S ^ A[i]

print(*ans)