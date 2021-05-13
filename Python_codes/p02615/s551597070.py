N = int(input())

A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0

ans += A[0]

cnt = 1
i = 1
#足せる回数はN-1回
while cnt < N-2:
    ans += A[i] * 2
    i += 1
    cnt += 2
if cnt == N-2:
    ans += A[i]

print(ans)
